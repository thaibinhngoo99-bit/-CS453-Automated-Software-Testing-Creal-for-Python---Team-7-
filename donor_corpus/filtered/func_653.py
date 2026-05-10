@ttfw_idf.idf_example_test(env_tag='Example_WIFI_Protocols')
def test_examples_protocol_asio_udp_server(env, extra_data):
    """
    steps: |
      1. join AP
      2. Start server
      3. Test connects to server and sends a test message
      4. Test evaluates received test message from server
      5. Test evaluates received test message on server stdout
    """
    test_msg = b'echo message from client to server'
    dut1 = env.get_dut('udp_echo_server', 'examples/protocols/asio/udp_echo_server', dut_class=ttfw_idf.ESP32DUT)
    binary_file = os.path.join(dut1.app.binary_path, 'asio_udp_echo_server.bin')
    bin_size = os.path.getsize(binary_file)
    ttfw_idf.log_performance('asio_udp_echo_server_bin_size', '{}KB'.format(bin_size // 1024))
    dut1.start_app()
    data = dut1.expect(re.compile(' IPv4 address: ([0-9]+\\.[0-9]+\\.[0-9]+\\.[0-9]+)'), timeout=30)
    cli = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    cli.settimeout(30)
    cli.connect((data[0], 2222))
    cli.send(test_msg)
    data = cli.recv(1024)
    if data == test_msg:
        print('PASS: Received correct message')
        pass
    else:
        print('Failure!')
        raise ValueError('Wrong data received from asio udp server: {} (expected:{})'.format(data, test_msg))
    dut1.expect(test_msg.decode())