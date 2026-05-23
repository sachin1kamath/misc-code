import Ollama from 'ollama';

async function displayResponse() {
    const responseDiv = document.getElementById('response');
    responseDiv.textContent = '';

    let input = String(document.getElementById('input').value);

    const response = await Ollama.chat({
        model: 'qwen3.5:9b',
        messages: [{ role: 'user', content: input }],
        stream: true,
    });
    for await (const part of response) {
        console.log(part.message.content)
        responseDiv.textContent += part.message.content;
    }
    const inputBox = document.getElementById('input');
    input.textContent = 'Input'
};

window.displayResponse = displayResponse;