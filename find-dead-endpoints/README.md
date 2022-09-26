## Purpose

Finds all method-names in an OpenAPI-definition and looks for calls of these methods (=== endpoints) in the frontend-code.

If a method is called 0 times, you might as well delete the endpoint.

## Usage

``` shell
fish find-dead-endpoints.fish /path/to/api /path/to/frontend-code
```

## Dependencies

- Fish
- Ripgrep
