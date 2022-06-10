% grpc Basics

- In gRPC, a client application can directly call a method on a server application on a different machine as if it were a local object thus creating distributed applications and services.
- Protocol Buffers are used as IDL (Interface Definition Language) as well as underlying message interchange format. 
- Define a service, with its expected parameters and return types. On ther server side this is implemented and a grpc server handles the client calls. On the client side a stub is defined based on the same interface. 
- In addition to Protocol buffers it is also possible to use json as the data format. 