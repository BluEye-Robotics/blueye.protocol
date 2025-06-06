import re
from pathlib import Path

from invoke import task


def strip_protolint_comments(file_path: Path):
    """
    Strip protolint comments from the given .proto file.

    Args:
        file_path (Path): The path to the .proto file.
    """
    # Read the content of the file
    with file_path.open("r") as file:
        content = file.read()

    # Define the regex pattern to match protolint comments
    pattern = r"protolint:disable:(next|this) [A-Z_]+"

    # Remove the protolint comments
    modified_content = re.sub(pattern, "", content)

    # Write the modified content back to the file
    with file_path.open("w") as file:
        file.write(modified_content)


def get_project_root_path() -> Path:
    """Get the project root path

    The tasks.py file (this file) always resides in the root of the project,
    therefore we can use it as a reference
    """
    return Path(__file__).parent


def gather_proto_files(proto_dir: Path) -> list[Path]:
    """Gather all .proto files in the given directory

    Args:
        proto_dir (Path): The directory to search for .proto files

    Returns:
        list[Path]: A list of paths to .proto files
    """
    return list(proto_dir.rglob("*.proto"))


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
        context.run("rm -rf build && mkdir -p build && mkdir -p build/protobuf_definitions")
        context.run("cp -r ProtocolDefinitions/protobuf_definitions/* build/protobuf_definitions/")
        proto_dir = get_project_root_path() / "build" / "protobuf_definitions"
        proto_files = gather_proto_files(proto_dir)
        for file in proto_files:
            strip_protolint_comments(file)
        context.run(
            "docker run \
            --mount type=bind,source=$(pwd)/build/protobuf_definitions/,destination=/in/ \
            --mount type=bind,source=$(pwd)/build/,destination=/out/ \
            --mount type=bind,source=$(pwd)/generators/templates/templates,destination=/templates/,readonly \
            --rm \
            --user $UID \
            blueyerobotics/gapic-generator-python:v1.21.0-fix-options \
            --python-gapic-templates /templates/ \
            --python-gapic-templates DEFAULT"  # noqa F501
        )
        context.run("cp -r build/blueye/protocol/types protocol/blueye/protocol/")
        context.run("cp -r build/blueye/protocol/__init__.py protocol/blueye/protocol/protos.py")


@task(pre=[generate_tcp, generate_udp])
def test(context):
    with context.cd(get_project_root_path()):
        context.run("pytest legacyprotocol/tests")
