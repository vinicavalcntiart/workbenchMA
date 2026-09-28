# Notas do laboratorio (bpy 5.2.2, escala real: cabeca raio 10 cm, fio 28 cm)

- 5.2: Interpolate acha o scalp pelo Object Data (surface + surface_uv_map). Attach Hair Curves to Surface com Named Attribute "UVMap" na frente QUEBRA (fios de 1 ponto): o UV e lido nas curvas.
- Density do Interpolate: painel trava em 10000/m2. Scalp real ~0,05 m2 -> ~420 fios. Value node no socket passa: 100000 -> 5088; 300000 -> ~15500.
- Clump (GD 2 cm, F 1): Shape 0 = careca na raiz; Shape 0,5 = so pontas; Shape 0,25 = mechas estilizadas com raiz coberta; Shape 1 = quase nada. Distance Falloff 0,006-0,01 apaga o clump.
- Mecha em fita: Shape 0 + Factor = Map Range(Spline Parameter, 0..0,3 -> 0..1, clamp) + Tip Spread 0,004. Rampa 0,15 abre buraco.
- Curl: voltas por metro = 3 x Frequency (Math.017 x3, Segment Length acumulado). Frequency 1 em fio de 28 cm = < 1 volta. Merida: Radius 0,01-0,011, Frequency 9-10. Mola apertada: Radius 0,007, Frequency 20. Subdivision 3 (12 pts -> 89 pts/fio, 1,1 M pontos em 13 mil fios).
- Ordem: Clump (Shape 0,25) > Curl com Existing Guide Map ligado = cacho acompanha a mecha. Curl sozinho ja funciona, mas sem definicao de mecha.
- Variacao de cacho: Random Value (Float) com ID = Named Attribute int guide_curve_index -> Radius 0,007-0,016 e Frequency 6-13. Por mecha mantem definicao. Por fio (ID vazio) vira massa felpuda.
- Ondas: Noise precisa de Scale ~10 e Scale along Curve ~8 em escala real (interno: Noise Texture Scale 5 x posicao da raiz x Scale). Curl f3 r1,5cm = onda de praia estilizada (helice). Onda plana "S": Subdivide 2 -> sin(2pi*Length/periodo + fase por mecha) * rampa(Spline Factor 0..0,2) * eixo lateral normalize(cross(Tangent, Z)) -> Set Position Offset. Amp 2 cm, periodo 12 cm = S limpo.
- Cor: Store Named Attribute (Float, Curve) "mecha_rand" = Random Value com ID guide_curve_index; no shader Attribute "mecha_rand" -> Map Range 0,3-0,65 -> Melanin. Por mecha = faixas de tom estilizadas. Hair Info Random (por fio) so suja. Raiz escura: Hair Info Intercept -> Map Range (0-0,25 -> +0,45 a 0, clamp) somado a melanina.
- Strays: Curve Info Random -> Compare Less Than 0,12 -> Factor do Frizz (Distance 0,02, Cumulative, Preserve Length). Com Trim Length Factor 1,25 no Mask fica realista/bagunçado. Frizz so na ponta com 4 mm nao aparece.
- Stray estilizado (arco limpo): Curve Info Random < 0,04 -> Factor do Hair Curves Noise (Distance 0,04, Shape 0,7, Scale 3, Offset per Curve 1, Cumulative ligado, Preserve Length). 7 cm = dramatico. Frizz = zigue-zague realista.
- Curve to Mesh 5.2: entrada Scale solta NAO usa o raio do fio (tubos de 1 m). Ligar node Radius no Scale.
