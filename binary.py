import random
from browser import document, aio
import asyncio


def is_web():
    return "__BRYTHON__" in globals()


def write(message, end='\n'):
    if is_web():
        console = document.getElementById('console')
        p = document.createElement('p')
        p.textContent = '> ' + message
        console.appendChild(p)
        console.scrollTop = console.scrollHeight
    else:
        print(message, end=end)


async def read():
    if is_web():
        inp = document.getElementById('input')
        while True:
            event = await aio.event(inp, 'keydown')
            if event.key == 'Enter':
                tmp = event.target.value
                event.target.value = ''
                write(tmp)
                return tmp
    else:
        return input()


def run(function):
    if is_web():
        aio.run(function())
    else:
        asyncio.run(function())


def generate_binary():
    binary = ""
    decimal = 0
    for _ in range(5):
        bit = random.randint(0, 1)
        binary += str(bit)
        decimal = decimal * 2 + bit
    return binary, decimal


def main():
    write(" " * 30 + "BINARY")
    write(" " * 15 + "CREATIVE COMPUTING  MORRISTOWN NEW JERSEY")
    write()
    write()

    for i in range(10):
        binary, decimal = generate_binary()
        write("BINARY:", end=" ")
        for j in range(5):
            write(binary[j], end=" ")
        write("     DECIMAL:", end=" ")
        user_input = int(read())

        if user_input == decimal:
            write("Correct!")
        else:
            write("Incorrect. The correct answer is:", decimal)

    write()
    write()

    for i in range(10):
        binary, decimal = generate_binary()
        print("DECIMAL:  ", decimal, end=" ")
        user_input = read()("     BINARY:   ")
        user_input = user_input.zfill(5)

        if user_input == binary:
            print("Correct!")
        else:
            print("Incorrect.")

    write()
    write()
    t0 = 20
    for i in range(10):
        t0 -= 1

    write("YOUR SCORE:", int(t0 / 0.2 + 0.5), "%")
    write()
    write()


run(main)
