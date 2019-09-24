from invoke import task
import toml


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
