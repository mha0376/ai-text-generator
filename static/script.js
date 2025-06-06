async function generateText() {
    const prompt = document.getElementById("prompt").value;
    const maxTokens = document.getElementById("maxTokens").value;
    const outputType = document.getElementById("outputType").value;
    const responseDiv = document.getElementById("response");

    console.log("Sending request:", { prompt, max_tokens: maxTokens, output_type: outputType });

    try {
        const response = await fetch("/generate", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ prompt, max_tokens: parseInt(maxTokens), output_type: outputType })
        });
        const data = await response.json();
        console.log("Received response:", data);
        if (data.error) {
            responseDiv.innerHTML = `<p style="color: red;">خطا: ${data.error}</p>`;
        } else {
            responseDiv.innerHTML = `<p>${data.response || "هیچ پاسخی از سرور دریافت نشد"}</p>`;
        }
    } catch (error) {
        console.log("Fetch error:", error);
        responseDiv.innerHTML = `<p style="color: red;">خطا: ${error.message}</p>`;
    }
}