import asyncio

# Runs a specific command in a separate subprocess.
async def run(command):
    process = await asyncio.create_subprocess_shell(
            command,
            stdout = asyncio.subprocess.PIPE,
            stderr = asyncio.subprocess.PIPE
    )

    output, errors = await process.communicate()

    print(f'[{command!r} exited with {process.returncode}]')

    if output:
        print(f'[output]\n{output.decode()}')

    if errors:
        print(f'[errors]\n{errors.decode()}')

# Runs the front-end related commands.
async def run_front_end_commands():
    await asyncio.gather(
            run("live-server --entry-file=source-code/html/index.html"),
            run("cd source-code && sass --watch sass:css")
    )

asyncio.run(run_front_end_commands())
