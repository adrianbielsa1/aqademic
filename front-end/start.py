import asyncio

# Runs a specific command in a separate subprocess.
async def run(command):
    process = await asyncio.create_subprocess_shell(
            command,
            stdout = asyncio.subprocess.PIPE,
            stderr = asyncio.subprocess.PIPE
    )

    output, errors = await process.communicate()

    print(f"[{command!r} exited with {process.returncode}]")

    if output:
        print(f"[output]\n{output.decode()}")

    if errors:
        print(f"[errors]\n{errors.decode()}")

# Auxiliar function to convert a dictionary into a flattened string, adding
# a = symbol between each key and its value, and a space between each key-value
# pair.
#
# Example input & output:
#
#   [in]    { a: 1, b: 2, c: [3, 4] }
#   [out]   a=1 b=2 c=3 c=4
def flatten_dictionary_into_string(d, concatenator, separator):
    s = ""

    for key, value in d.items():
        if isinstance(value, str):
            s += key + concatenator + value
        elif isinstance(value, list):
            for inner_value in value:
                s += key + concatenator + inner_value

        # A space to separate each argument.
        s += separator

    return s

# Runs the front-end related commands.
async def run_front_end_commands():
    live_server_arguments = {
        "--port": "8080",
        "--entry-file": "source-code/html/index.html",

        # A few aliases so the URL doesn't show the inner folder structure
        # unless explicitly accessed.
        "--mount": [
            "/login:source-code/html/login.html",
        ],
    }

    sass_arguments = {
        "--watch": "source-code/sass:source-code/css"
    }

    commands = [
        "live-server " + flatten_dictionary_into_string(live_server_arguments, "=", " "),
        "sass " + flatten_dictionary_into_string(sass_arguments, " ", " ")
    ]

    # Display the list of commands.
    for command in commands:
        print("[run] " + command)

    # Apply the `run` function to each `command`, and then unpack these async
    # calls and wait for them to complete with `gather`.
    await asyncio.gather(*map(run, commands))

asyncio.run(run_front_end_commands())
