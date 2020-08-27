> What is TorchScript?
> It is a way to create serializable and optimizable models from PyTorch code. 
> Train model in PyTorch (python) -> Export model via Torchscript -> Run it in a standalone C++ program

**References**
[1] [Introduction to Torchscript](https://pytorch.org/tutorials/beginner/Intro_to_TorchScript_tutorial.html)
[2] [Loading a Torchscript model in C++](https://pytorch.org/tutorials/advanced/cpp_export.html)

Summary of [2]

* Step 1 - Converting your PyTorch Model to Torch Script
	* Tracing - structure of the model is captured by evaluating the model it once using example inputs and recording the flow of the inputs through the model. (suitable for models with limited use of control flow)
	* Explicit annotations - Torchscript compiler directly parse and compile the model code. 

	```python
	
	import torch
	import torchvision
	
	model = torchvision.models.resnet18()
	example = torch.rand(1, 3, 224, 224)
	traced_script_module = torch.jit.trace(model, example)
	
	```
* Step 2 - Serializing your Script Module to a File

```python
traced_script_module.save("mymodel.pt")
```
* Step 3 - Loading your Script Module in C++

```C++
#include <torch/script.h>

#include <iostream>
#include <memory>

int main(int argc, char* argv[])
{
	torch::jit::script::Module module;
	try {
		module = torch::jit::load(argv[1]);
	} 
	catch(const c10::Error& e) {
		std::err << "Error loading the model";
		return -1;
	}
	return 0;
}
```

```cmake
cmake_minimum_required(VERSION 3.0 FATAL_ERROR)
project(custom_ops)

find_package(Torch REQUIRED)

add_executable(example-app example-app.cpp)
target_link_libraries(example-app "${TORCH_LIBRARIES}")
set_property(TARGET example-app PROPERTY CXX_STANDARD 14)
```

* Step 4 - Executing the script module in C++

```c++
// Create a vector of inputs.
std::vector<torch::jit::IValue> inputs;
inputs.push_back(torch::ones({1, 3, 224, 224}));

// Execute the model and turn its output into a tensor.
at::Tensor output = module.forward(inputs).toTensor();
std::cout << output.slice(/*dim=*/1, /*start=*/0, /*end=*/5) << '\n';
```

