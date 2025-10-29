import discord
import random

# --- Configuración del bot ---
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# --- Elementos para generar contraseñas ---
elements = "+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

# --- Diccionario de memes ---
meme_dict = {
    "CRINGE": "Algo excepcionalmente raro o embarazoso",
    "LOL": "Una respuesta común a algo gracioso",
    "BACANO": "Algo que está muy chévere",
}

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # --- Comando $hello ---
    if message.content.startswith('$hello'):
        await message.channel.send("¡Hola! 👋")

    # --- Comando $bye ---
    elif message.content.startswith('$bye'):
        await message.channel.send("😊")

    # --- Comando $pass <longitud> ---
    elif message.content.startswith('$pass'):
        try:
            parts = message.content.split()
            if len(parts) < 2:
                await message.channel.send("Por favor, indica la longitud. Ejemplo: `$pass 12`")
                return

            pass_length = int(parts[1])
            password = ''.join(random.choice(elements) for _ in range(pass_length))
            await message.channel.send(f"🔐 Tu contraseña generada es:\n`{password}`")
        except ValueError:
            await message.channel.send("Debes escribir un número entero. Ejemplo: `$pass 10`")

    # --- Comando $meme <PALABRA> ---
    elif message.content.startswith('$meme'):
        parts = message.content.split()
        if len(parts) < 2:
            await message.channel.send("Por favor, escribe una palabra. Ejemplo: `$meme LOL`")
            return

        word = parts[1].upper()
        if word in meme_dict.keys():
            await message.channel.send(f"📖 **{word}**: {meme_dict[word]}")
        else:
            await message.channel.send("❌ Todavía no tenemos esta palabra... Pero estamos trabajando en ello 🧠")

    elif message.content.startswith('$sarcasmo'):
        frases = [
            "Wow, qué aporte tan revolucionario...",
            "Seguramente la NASA te está llamando en este momento.",
            "Eso suena totalmente creíble, sí claro.",
            "Excelente, otro genio incomprendido en el chat.",
            "Sí, porque eso *obviamente* iba a funcionar.",
            "¿Y si pruebas usar el cerebro la próxima vez?",
            "Increíble, ni ChatGPT se atrevería a tanto."
        ]
        respuesta = random.choice(frases)
        await message.channel.send(respuesta)

    else:
        await message.channel.send("Comando no reconocido. Usa `$hello`, `$bye`, `$sarcasmo`, `$pass <n>` o `$meme <PALABRA>`")

# --- Ejecutar el bot ---
client.run("TOKEN")
