import gradio as gr

# Linear Search Function
def linear_search_ui(numbers, target):
    try:
        # Convert input into list of integers
        arr = [int(x.strip()) for x in numbers.split(",")]
        # Convert input to integer
        target = int(target)

        # Loop through each element in list
        for i in range(len(arr)):
            # Check if current element matches target
            if arr[i] == target:
                return f"Found at index {i}"

        # If loop finishes w/o finding target
        return "Not found"
    
    except:
        # Invalid input
        return "Invalid input"

# Gradio UI
with gr.Blocks() as demo:
    gr.Markdown("## Linear Search App")

    numbers_input = gr.Textbox(label="Enter numbers (comma separated)")
    target_input = gr.Textbox(label="Enter number to search")

    output = gr.Textbox(label="Result")

    btn = gr.Button("Search")

    btn.click(fn=linear_search_ui, inputs=[numbers_input, target_input], outputs=output)

demo.launch()
