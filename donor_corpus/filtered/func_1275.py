@client.event
async def on_message(message):
    if message.author == client.user:
        return
    wordbank = ['cat', 'puppy', 'bunny', 'giraffe', 'poop']
    if message.content == 'pycascade':
        response = 'Hello everyone! Welcome and have a great time!'
        await message.channel.send(response)
    elif message.content in wordbank:
        await message.channel.send("please don't use bad words")
    elif 'pokemon' in message.content:
        pokemon = message.content.split()[1]
        req = requests.get(f'https://getpokemonweakness.azurewebsites.net/api/getweakness?pokemon={pokemon}')
        await message.channel.send(req.content)