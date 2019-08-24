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


@task(pre=[generate_tcp, generate_udp])
def test(context):
    context.run("pytest blueye/protocol/tests")
