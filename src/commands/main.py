import voltage

client = voltage.Client()  # Initialize the client.


@client.listen("ready")  # Listen to an event.
async def on_ready():
    print(f"Logged in as {client.user}")


@client.listen("message")
async def on_message(message):  # Doesn't matter what you call the function.
    if message.content == "-ping":
        await message.channel.send("pong!")  # Send a message.
    elif message.content == "-embed":
        embed = voltage.SendableEmbed(title="Hello World", description="This is an embed")  # Create an embed.
        # Reply to a message.
        await message.reply(content="embed", embed=embed)  # Obligatory message content.

# Run the client which is an abstraction of calling the start coroutine.
client.run("hcM4odMOmoTRwAAddaLgr4x1CwUsc3jl0okInDNJQ_55N3iUFWlRUwQFIy5hP2_d")  # Replace with your token.