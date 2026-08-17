Protótipo Academico

# Sistema de Detecção de Uniformes

## 🎯 Objetivo

Este projeto foi desenvolvido durante o curso de Desenvolvimento de Sistemas do SENAI com o objetivo de criar um sistema capaz de identificar, por meio de imagens, se uma pessoa estava utilizando um uniforme.

A proposta era utilizar visão computacional para reconhecer o símbolo presente no uniforme e auxiliar na identificação de pessoas que estivessem ou não utilizando a vestimenta adequada.

## 💻 Tecnologias utilizadas

- Python
- OpenCV
- ORB (Oriented FAST and Rotated BRIEF)
- Processamento de imagens

## ⚙️ Funcionamento

O sistema recebe uma imagem e realiza uma comparação entre ela e uma imagem de referência do símbolo do uniforme.

Por meio do OpenCV e do algoritmo ORB, são identificados pontos de interesse nas imagens. Esses pontos são comparados para verificar se existem características semelhantes suficientes para considerar que o símbolo foi identificado.

## 📚 O que aprendi

Durante o desenvolvimento, aprendi conceitos de processamento e reconhecimento de imagens utilizando Python e OpenCV.

Também pude compreender melhor os desafios envolvidos em sistemas de visão computacional, principalmente em situações com diferentes condições de iluminação e desgaste do uniforme.

O projeto também ajudou a desenvolver conhecimentos sobre testes, análise de erros e aprimoramento de soluções durante o desenvolvimento de software.

## ⚠️ Observações

Este projeto foi desenvolvido como um protótipo acadêmico. Durante os testes, o sistema apresentou limitações no reconhecimento em algumas situações, como quando o uniforme estava desbotado ou quando havia diferenças significativas nas imagens.
