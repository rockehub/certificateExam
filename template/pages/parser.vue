<template>
  <div>
    <h1>Parser de Questões</h1>
    <textarea v-model="inputText" placeholder="Cole as questões aqui" rows="10" cols="50"></textarea>
    <button @click="parseQuestions">Adicionar ao JSON</button>
    <button @click="clearJson">Limpar JSON</button>
    <button @click="removeLastQuestion">Remover Última Questão</button>
    <pre>{{ JSON.stringify(parsedQuestions, null, 2) }}</pre>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';

const inputText = ref('');

interface Question {
  Question: string;
  QuestionText: string;
  Options: string[];
  CorrectAnswer: string[];
}

const parsedQuestions = ref<Question[]>([]);

const parseQuestions = (): void => {
  const questionsArray = inputText.value.trim().split(/\n\n/);
  questionsArray.forEach((q) => {
    const lines = q.split('\n');
    const questionNumberMatch = lines[0].match(/Question: (\d+)/);
    if (!questionNumberMatch) return;

    const questionNumber = questionNumberMatch[1];
    let questionText = '';
    const options: string[] = [];
    let correctAnswers: string[] = [];

    for (let i = 1; i < lines.length; i++) {
      if (lines[i].match(/^\d+\.\)/)) {
        options.push(lines[i]);
      } else if (lines[i].startsWith('Correct Answer:')) {
        correctAnswers = lines[i].split(': ')[1].split(',').map((answer) => answer.trim());
      } else {
        questionText += (questionText ? ' ' : '') + lines[i].trim();
      }
    }

    parsedQuestions.value.push({
      Question: questionNumber,
      QuestionText: questionText,
      Options: options,
      CorrectAnswer: correctAnswers
    });
  });
  inputText.value = '';
};

const clearJson = (): void => {
  parsedQuestions.value = [];
};

const removeLastQuestion = (): void => {
  parsedQuestions.value.pop();
};
</script>

<style>
textarea {
  width: 100%;
  margin-bottom: 10px;
}
button {
  display: block;
  margin-bottom: 10px;
}
</style>
