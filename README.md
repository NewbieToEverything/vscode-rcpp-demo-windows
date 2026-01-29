# vscode-rcpp-demo

This project is a combination of [vscode-rcpp-demo](https://github.com/renkun-ken/vscode-rcpp-demo) and [gdb_armadillo_helpers](https://github.com/darcamo/gdb_armadillo_helpers), hosting a minimal example of writing and debugging [Rcpp](http://www.rcpp.org/) in VScode in windows with pretty printers for armadillo vectors, matrices and cubes, as well as a few xmethods. 

Thank [Kun](https://renkun.me/) and [Darlan](https://github.com/darcamo) for developing such two useful workflows. 

## Setup

1. Download or clone this repo to your local machine.
2. Follow Kun's instruction in [vscode-rcpp-demo](https://github.com/renkun-ken/vscode-rcpp-demo).
3. Set breakpoints in `src/test.cpp` (for example, line 11).
4. Start debugging (F5) and have fun.

**NOTE**: 

- To apply this setup to your own Rcpp scripts housed in an R package, you may follow the instruction below:
  1. copy the `gdb_configuration/` and `.vscode/` folders to your project root folder, and change the paths in `c_cpp_properties.json` (line 7, 8, 9, 12), `.vscode/launch.json` (line 8), and `task.json` (line 7) accordingly.
  2. modify the `tests/testthat.R` file to load your own package, and add test files in the `tests/testthat/` folder to trigger the compilation and execution of your Rcpp functions. For more details about the testthat framework, please refer to the [testing chapter](https://r-pkgs.org/testing-basics.html) in the R Packages book by Hadley Wickham.
- Instead of using the `.gdbinit` file to load the pretty printers as in the original [gdb_armadillo_helpers](https://github.com/darcamo/gdb_armadillo_helpers) repo, I have modified the `launch.json` file in the `.vscode` folder to load the pretty printers automatically when starting a debugging session in VScode. If you clone this repo, you don't need to change anything. If you modify the folder structure of `gdb_configuration/`, please change the path in line 27 of `.vscode/launch.json` accordingly.
- This debug setup has only been tested in Windows 11, because I don't have a Linux or Mac machine. If you have successfully applied this setup in Linux or Mac, please feel free to open a PR to share your experience.