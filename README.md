# vscode-rcpp-demo

This project is a combination of [vscode-rcpp-demo](https://github.com/renkun-ken/vscode-rcpp-demo) and [gdb_armadillo_helpers](https://github.com/darcamo/gdb_armadillo_helpers), hosting a minimal example of writing and debugging [Rcpp](http://www.rcpp.org/) in VScode in windows with pretty printers for armadillo vectors, matrices and cubes, as well as a few xmethods. 

Thank [Kun](https://renkun.me/) and [Darlan](https://github.com/darcamo) for developing such two useful workflows. 

## Setup

1. Download or clone this repo to your local machine.
2. Follow Kun's instruction in [vscode-rcpp-demo](https://github.com/renkun-ken/vscode-rcpp-demo).

**NOTE**: Instead of using the `.gdbinit` file to load the pretty printers as in the original [gdb_armadillo_helpers](https://github.com/darcamo/gdb_armadillo_helpers) repo, I have modified the `launch.json` file in the `.vscode` folder to load the pretty printers when starting a debugging session in VScode. If you clone this repo, you don't need to change anything. Otherwise, please change the path in line 27 of `.vscode/launch.json` accordingly.