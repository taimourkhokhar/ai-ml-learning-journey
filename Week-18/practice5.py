# def simple_gen():
#   yield "Emil"
#   yield "Tobias"
#   yield "linux"

# gen=simple_gen()
# print(next(gen))
# print(next(gen))
# print(next(gen))

# def echo_generator():
#   while True:
#     received = yield
#     print("Received:", received)

# gen = echo_generator()
# next(gen) # Prime the generator
# gen.send("Hello")
# gen.send("World")

# def my_gen():
#   try:
#     yield 1
#     yield 2
#     yield 3
#   finally:
#     print("Generator closed")

# gen = my_gen()
# print(next(gen))
# gen.close()