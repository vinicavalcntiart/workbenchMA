@echo off
title Instalador VC_Smooth
REM ============================================================
REM  VC_Smooth - instalador para Windows
REM  Baixa o Blender, aplica o patch e compila. Rode uma vez.
REM  Requisitos: Git e Visual Studio 2022 Community com o
REM  workload "Desktop development with C++" instalados.
REM ============================================================
setlocal
set "BASE_BRANCH=blender-v5.2-release"
set "SCRIPT_DIR=%~dp0"
set "LOG=%SCRIPT_DIR%instalacao_log.txt"
echo Instalacao VC_Smooth iniciada > "%LOG%"

where git >nul 2>nul
if errorlevel 1 goto no_git

if not exist "%SCRIPT_DIR%zbrush-style-smooth.patch" goto no_patch

cd /d "%USERPROFILE%"
if exist "blender-vc\blender\.git" goto ja_clonado

echo [1/4] Clonando o Blender... isso demora varios minutos, deixa rodando.
git clone https://projects.blender.org/blender/blender.git "blender-vc\blender" >> "%LOG%" 2>&1
if errorlevel 1 goto erro_clone

:ja_clonado
cd /d "%USERPROFILE%\blender-vc\blender"

echo [2/4] Mudando para o Blender 5.2 LTS...
git fetch origin %BASE_BRANCH% >> "%LOG%" 2>&1
git checkout -B vc-smooth origin/%BASE_BRANCH% >> "%LOG%" 2>&1
if errorlevel 1 echo AVISO: nao consegui fixar o commit base, seguindo com a versao atual.

echo [3/4] Aplicando o patch VC_Smooth...
git apply --check "%SCRIPT_DIR%zbrush-style-smooth.patch" >> "%LOG%" 2>&1
if errorlevel 1 goto erro_patch
git apply "%SCRIPT_DIR%zbrush-style-smooth.patch" >> "%LOG%" 2>&1
if errorlevel 1 goto erro_patch

echo [4/4] Baixando bibliotecas e compilando... 30 a 90 min na primeira vez.
echo        O progresso aparece nesta janela. NAO FECHE.
call make.bat update
if errorlevel 1 goto erro_build
call make.bat
if errorlevel 1 goto erro_build

echo.
echo ============================================================
echo  PRONTO! O Blender modificado esta em:
echo  %USERPROFILE%\blender-vc\build_windows_x64_vc17_Release\bin\Release\blender.exe
echo  Se nao estiver ai, procure a pasta build_windows_... em
echo  %USERPROFILE%\blender-vc
echo  Agora importe o brush VC_Smooth_brush.blend - veja o README.
echo ============================================================
goto fim

:no_git
echo ERRO: Git nao encontrado. Instale em https://git-scm.com e rode de novo.
goto fim

:no_patch
echo ERRO: o arquivo zbrush-style-smooth.patch precisa estar na mesma pasta deste .bat.
goto fim

:erro_clone
echo ERRO ao clonar o Blender. Veja o arquivo instalacao_log.txt nesta pasta.
goto fim

:erro_patch
echo ERRO: o patch nao aplicou nesta versao. Veja instalacao_log.txt e me avisa que eu regenero.
goto fim

:erro_build
echo ERRO na compilacao. Causa mais comum: Visual Studio 2022 com o workload
echo "Desktop development with C++" nao instalado. Veja instalacao_log.txt.
goto fim

:fim
echo.
pause
