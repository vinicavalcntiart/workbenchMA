@echo off
REM ============================================================
REM  VC_Smooth - instalador para Windows
REM  Baixa o Blender, aplica o patch e compila. Rode uma vez.
REM  Requisitos: Git e Visual Studio 2022 Community com o
REM  workload "Desktop development with C++" instalados.
REM ============================================================
setlocal
set BASE_COMMIT=08bed5b5b42ec017e8dcc87b76f6c373c322b086
set SCRIPT_DIR=%~dp0

where git >nul 2>nul
if errorlevel 1 (
  echo [ERRO] Git nao encontrado. Instale em https://git-scm.com e rode de novo.
  pause & exit /b 1
)

if not exist "%SCRIPT_DIR%zbrush-style-smooth.patch" (
  echo [ERRO] zbrush-style-smooth.patch precisa estar na mesma pasta deste .bat.
  pause & exit /b 1
)

cd /d %USERPROFILE%
if not exist blender-vc\blender (
  echo [1/4] Clonando o Blender (demora um pouco)...
  git clone https://projects.blender.org/blender/blender.git blender-vc\blender || (pause & exit /b 1)
)
cd blender-vc\blender

echo [2/4] Fixando na versao base do patch...
git fetch origin %BASE_COMMIT% 2>nul
git checkout %BASE_COMMIT% || echo [AVISO] Nao consegui fixar o commit base; seguindo com a versao atual.

echo [3/4] Aplicando o patch VC_Smooth...
git apply --check "%SCRIPT_DIR%zbrush-style-smooth.patch" && git apply "%SCRIPT_DIR%zbrush-style-smooth.patch"
if errorlevel 1 (
  echo [ERRO] O patch nao aplicou. Me avisa que eu regenero para a sua versao.
  pause & exit /b 1
)

echo [4/4] Baixando bibliotecas e compilando (30-90 min na primeira vez)...
call make.bat update || (pause & exit /b 1)
call make.bat || (pause & exit /b 1)

echo.
echo ============================================================
echo  PRONTO! O Blender modificado esta em:
echo  %USERPROFILE%\blender-vc\build_windows_*\bin\Release\blender.exe
echo  Agora importe o brush: veja o README (passo "Importar o brush").
echo ============================================================
pause
