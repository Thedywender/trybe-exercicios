let nota = 20;
 if(nota < 1 || nota > 100) {
    console.log("digite uma nota válida")
} else if (nota >= 80 && nota <= 100){
    console.log("Parabéns você faz parte do grupo de pessoas aprovadas")
} else if(nota >= 60 && nota < 80) {
    console.log("Você está na nossa lista de espera");
} else {
    console.log("infelizmente você foi reprovada")
} 