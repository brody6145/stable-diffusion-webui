@echo off

rem Enable DirectML support in PyTorch
set PYTORCH_ENABLE_DIRECTML=1

rem Set arguments to disable CUDA and enable DirectML
set COMMANDLINE_ARGS=--skip-torch-cuda-test --no-half --use-directml

rem Launch the WebUI
call webui.bat
