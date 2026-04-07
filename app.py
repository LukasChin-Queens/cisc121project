import gradio as gr

# Linear Search Function
def linear_search_ui(numbers, target):
    try:
        # Convert input into list of integers
        arr = [int(x.strip()) for x in numbers.split(",")]
        # Convert input to integer
        target = int(target)
        steps = ""
        
        # Loop through each element in list
        for i in range(len(arr)):
            
            # Counting steps
            steps += f"Step {i+1}: Checking index {i} (value = {arr[i]})\n"
            
            # Check if current element matches target
            if arr[i] == target:
                steps += f"\n✅ Found {target} at index {i}"
                return steps

        # If loop finishes w/o finding target
        steps += f"\n❌ {target} not found in the list"
        return steps
    
    except:
        # Invalid input
        return "Invalid input"

# Gradio UI
with gr.Blocks() as demo:
    gr.Markdown("## Linear Search App")
    gr.Markdown("Enter a list of numbers and a target. The app will show each step of the search process.")

    # Input
    numbers_input = gr.Textbox(
        label="Enter numbers (comma separated)",
        placeholder="e.g. 1, 5, 3, 9"
    )
    target_input = gr.Textbox(label="Enter number to search")

    #Output
    output = gr.Textbox(
        label="Search Steps",
        lines=3
    )

    btn = gr.Button("Search")

    btn.click(fn=linear_search_ui, inputs=[numbers_input, target_input], outputs=output)

demo.launch()
