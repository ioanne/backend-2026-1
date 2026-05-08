import asyncio


# def foo(arg):
#     return arg

# print(foo("Hola"))

async def foo2(arg):
    print(arg)
    return arg

# async def foo3(arg):
#     return await foo2("Hola")


asyncio.run(foo2("Hola"))
# Multi Tasking
    # Multi threading
    # Multi core
    # Asincronica (Un unico loop)