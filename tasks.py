from pathlib import Path

import toml
from invoke import task
from packaging.utils import canonicalize_name


def get_project_root_path() -> Path:
    """Get the projet root path

    The tasks.py file (this file) always resides in the root of the project,
    therefore we can use it as a reference
    """
    return Path(__file__).parent


@task
def generate_tcp(context):
    """
    Generate TCP protocol
    """
    import generators.generate_tcp_protocol

    protocol_context = generators.generate_tcp_protocol.Context()
    generators.generate_tcp_protocol.write_tcp_protocol(protocol_context)


@task
def generate_udp(context):
    """
    Generate UDP protocol
    """
    import generators.generate_udp_protocol

    generators.generate_udp_protocol.generate()


@task
def generate_proto(context):
    """
    Generate the Protobuf based protocol

    Uses the gapic-generator-python docker container, and therefore requires the user to have docker
    installed.
    """
    with context.cd(get_project_root_path()):
        context.run("rm -rf build && mkdir -p build")
        context.run(
            "docker run \
            --mount type=bind,source=$(pwd)/ProtocolDefinitions/protobuf_definitions/,destination=/in/ \
            --mount type=bind,source=$(pwd)/build/,destination=/out/ \
            --rm \
            --user $UID \
            gcr.io/gapic-images/gapic-generator-python:v0.40"  # noqa F501
        )
        context.run("cp -r build/blueye/protocol/types blueye/protocol/")
        context.run("cp -r build/blueye/protocol/__init__.py blueye/protocol/protos.py")


@task(pre=[generate_tcp, generate_udp])
def test(context):
    context.run("pytest tests")


@task
def generate_setup_py(context):
    context.run("poetry build")
    pyproject = toml.load("pyproject.toml")
    package_name = pyproject["tool"]["poetry"]["name"]
    package_version = pyproject["tool"]["poetry"]["version"]
    canonicalized_name = canonicalize_name(package_name)
    distribution_name = canonicalized_name.replace("-", "_")
    context.run(
        f"tar --extract --file=dist/{distribution_name}-{package_version}.tar.gz "
        + '--no-anchored "setup.py" --strip-components 1'
    )
