def mode():
    port_direction = ''
    for i in range(8):
        mode = input(f'Enter the direction for pin {i}: ').lower()
        if mode == 'in':
            port_direction += '0'
        elif mode == 'out':
            port_direction += '1'
        else:
            print('Invalid input, Please enter "in" or "out"!')
            return None
    return port_direction

def init_port():
    port_direction = mode()
    if port_direction is not None:
        print(f"""\
void Init_PORTA_DIR (void)
{{
    DDRA = 0b{port_direction[::-1]};
}}""")

init_port()