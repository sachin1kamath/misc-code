import Ollama from 'ollama';

async function getInput() {
    let input = String(document.getElementById('input').value);

    const response = await ollama.chat({
        model: 'qwen3.5:9b',
        messages: [{ role: 'user', content: input }],
    });
    console.log(response.message.content);
    return input;
};

function displayResponse(response) {
    const responseDiv = document.getElementById('response');
    responseDiv.innerHTML = `<p>${String(response)}</p>`;
};

window.displayResponse = displayResponse;
window.getInput = getInput; 