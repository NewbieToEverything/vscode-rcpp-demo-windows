# vscode-rcpp-demo

This project is a combination of [vscode-rcpp-demo](https://github.com/renkun-ken/vscode-rcpp-demo) and [gdb_armadillo_helpers](https://github.com/darcamo/gdb_armadillo_helpers), hosting a minimal example of writing and debugging [Rcpp](http://www.rcpp.org/) in VScode in windows with pretty printers for armadillo vectors, matrices and cubes, as well as a few xmethods. 

Thank [Kun](https://renkun.me/) and [Darlan](https://github.com/darcamo) for developing such two useful workflows. 

for autoloading: 
- create a directory called anything you fancy in c:/users/yourusername, where yourusername is your Windows username. Now from the control panel invoke the environment variables dialog and create a new environment variable called HOME. Set that variable to the above folder by clicking browse for folder and navigating there. Put .gdbinit in there and use it to set any autoload or other behaviour as you choose. When GDB starts it will now look in that folder for a .gdbinit file and load it.

for manually loading
after activating debug mode, enter the following command in the debug console, this works for the current debugging thread only
-exec source D:\cpp\HMCDM_FORGETTING\gdb_configuration\.gdbinit

## Preview

* Code editing

![Code editing](https://user-images.githubusercontent.com/4662568/71535253-8f2d2380-293f-11ea-920e-8a58a944fb50.gif)

* Debugging



## Configuration

If you are new to C++ and VScode, please refer to [C/C++ for Visual Studio Code](https://code.visualstudio.com/docs/languages/cpp) for detailed instruction.

The following extensions need to be installed: 

-[R](https://marketplace.visualstudio.com/items?itemName=REditorSupport.r)
-[C/C++](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools)

### Code editing

For C/C++ source code editing, only `.vscode/c_cpp_properties.json` is needed. When the proper paths of included headers are
provided, the full-featured C/C++ editing features including auto-completion, hover, definition, type inference, etc. will work.
Source code editing does not require that the code is in a package.

In this repo, `c_cpp_properties.json` is supposed to work with R 4.0 under Ubuntu 16.04 or above. You may need to alter the
paths according to your system and C/C++ dependencies of your package.

For example, if your package depends on [RcppArmadillo](https://github.com/RcppCore/RcppArmadillo), you may run the following R
code to determine the include path:

```r
RcppArmadillo:::CxxFlags()
```

Then you may add the following path to `includePath`:

```text
${env:HOME}/R/x86_64-pc-linux-gnu-library/4.0/RcppArmadillo/include
```

For more code editing features, please visit [Edit C++ in Visual Studio Code](https://code.visualstudio.com/docs/cpp/cpp-ide).

### Debugging

Rcpp debugging is easy to configure when the code is in an R package that uses Rcpp like how this repo is organized.

Since `R` is not a binary executable but a bash script in which required environment variables are setup to start an R session,
we also need to setup those environment variables for the debugger to run the R session.

`.vscode/debug.R` and `.vscode/tasks.json` are the code to capture those environment variables and to run before debugging.
You may need, initially, to run twice in debugging mode before environment variables are properly picked up in `.vscode/.env`

`.vscode/launch.json` defines the debugger configuration which in this repo works for R 4.0 under Ubuntu 16.04 or above.

For more debugging features, please visit [Debug C++ in Visual Studio Code](https://code.visualstudio.com/docs/cpp/cpp-debug).

### Pretty printer

for autoloading,: 
- create a directory called anything you fancy in c:/users/yourusername, where yourusername is your Windows username. Now from the control panel invoke the environment variables dialog and create a new environment variable called HOME. Set that variable to the above folder by clicking browse for folder and navigating there. Put .gdbinit in there and use it to set any autoload or other behaviour as you choose. When GDB starts it will now look in that folder for a .gdbinit file and load it.

for manually loading
after activating debug mode, enter the following command in the debug console, this works for the current debugging thread only
-exec source D:\cpp\HMCDM_FORGETTING\gdb_configuration\.gdbinit
