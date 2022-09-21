import toml
from invoke import task


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
    """
    context.run(
        "protoc \
            --proto_path ProtocolDefinitions/protobuf_definitions/ \
            --python_betterproto_out=build \
            ProtocolDefinitions/protobuf_definitions/*.proto")
    context.run("cp -r build/blueye/protocol/__init__.py blueye/protocol/v3/")


@task(pre=[generate_tcp, generate_udp])
def test(context):
    context.run("pytest tests")


@task
def generate_setup_py(context):
    context.run("poetry build")
    pyproject = toml.load("pyproject.toml")
    package_name = pyproject["tool"]["poetry"]["name"]
    package_version = pyproject["tool"]["poetry"]["version"]
    context.run(
        f'tar --extract --file=dist/{package_name}-{package_version}.tar.gz ' +
        '--no-anchored "setup.py" --strip-components 1')
