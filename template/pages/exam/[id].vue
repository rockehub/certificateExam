<template>
  <div class="container mb-50">
    <h1>{{ exam.name }} Exam</h1>
    <div v-if="exam.questions.length === 0" class="alert alert-warning">
      No questions found for this exam.
    </div>
    <div v-for="(question, questionIndex) in selectedQuestions" :key="questionIndex"
         :class="['card', { 'border-danger': !isQuestionCorrect(question) && examCompleted && questionHasInteraction(questionIndex) }]">
      <div class="card-header">
        <div class="d-flex justify-content-between" >
          <div style="max-width: 80%">
            <h5>N{{questionIndex +1}}</h5>
            <h4>{{ question.QuestionText }}</h4>
          </div>
          <div class="d-flex- justify-content-end">
            <button @click="checkQuestion(question)" class="btn btn-primary"> check question</button>
          </div>

        </div>


       <VCodeBlock v-if="question.Code" highlightjs  :code="question.Content" :lang="question.Lang" theme="github-dark-dimmed"/>
      </div>
      <div class="card-body">
        <div v-if="isSingleAnswer(question)">
          <div v-for="(option, optionIndex) in question.Options" :key="optionIndex" class="form-check">
            <input type="radio"
                   class="form-check-input"
                   :id="`${questionIndex}-${optionIndex + 1}`"
            :value="optionIndex + 1"
            v-model="selectedAnswer[questionIndex]"
            @change="updateInteraction(questionIndex)"
            >
            <label class="form-check-label" :for="`${questionIndex}-${optionIndex + 1}`">{{ option }}</label>
          </div>
        </div>
        <div v-else>
          <div v-for="(option, optionIndex) in question.Options" :key="optionIndex" class="form-check">
            <input type="checkbox"
                   class="form-check-input"
                   :id="`${questionIndex}-${optionIndex + 1}`"
            :value="optionIndex + 1"
            v-model="selectedAnswers[questionIndex][optionIndex]"
            @change="updateInteraction(questionIndex)"
            >
            <label class="form-check-label" :for="`${questionIndex}-${optionIndex + 1}`">{{ option }}</label>
          </div>
        </div>
      </div>
    </div>
    <div class="d-flex gap-2 justify-content-center">
      <button class="btn btn-primary mt-3" @click="submitExam">Finish Exam</button>
      <NuxtLink to="/" class="btn btn-secondary mt-3" >Back To List</NuxtLink>
    </div>

    <div v-if="examCompleted" class="mt-3">
      <h3 v-if="passed">Congratulations! You passed the exam. {{finalScore}}</h3>
      <h3 v-else>Sorry, you did not pass the exam.</h3>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import type { Exam, Question } from '@/types'; // Defina seus tipos TypeScript
import examsData from '@/static/exams.json'; // Importe os dados do exame
import VCodeBlock from '@wdns/vue-code-block';
import hljs from 'highlight.js/lib/core';
hljs.registerLanguage('impex', function (hljs) {
  return {
    name: 'Impex',
    case_insensitive: true,  // Impex is case insensitive
    keywords: {
      keyword: 'INSERT INSERT_UPDATE UPDATE REMOVE DELETE',
      literal: 'true false null',
      built_in: '$START_USERRIGHTS $END_USERRIGHTS $lang $configProperty $contentCatalog $contentCV $macro $catalog-id $catalog-version $catalogversion',  // Impex variables
    },
    contains: [
      hljs.COMMENT('#', '$'),  // Comments in Impex start with #
      {
        className: 'section',
        begin: /\b(?:INSERT|INSERT_UPDATE|UPDATE|REMOVE|DELETE)\b/,  // Commands like INSERT, UPDATE, etc.
        end: /;/,  // Commands generally end with a semicolon
        contains: [
          hljs.QUOTE_STRING_MODE,  // Strings enclosed in quotes
          {
            className: 'attribute',
            begin: /\b[A-Za-z][A-Za-z0-9]*(\([\w\.\:\[\]\=\-]+\))?\b/,  // Matches the attribute names with optional modifiers
            relevance: 0
          },
          {
            className: 'operator',
            begin: /[+=|<>.-]+/,  // Operators used in Impex expressions
            relevance: 0
          }
        ]
      },
      {
        className: 'variable',
        begin: /\$[A-Za-z_-][A-Za-z0-9_-]*\b/,  // Matches Impex variables
        relevance: 10
      },
      {
        className: 'params',
        begin: /\b(?:unique|default|lang)\s*=\s*[^\s;]+/,  // Matches Impex modifiers like unique=true or default=$catalog-id:$catalog-version
        keywords: 'unique default lang',
        relevance: 10
      },
      {
        className: 'literal',
        begin: /\b(true|false|null)\b/,  // Literal values
        relevance: 0
      },
      hljs.QUOTE_STRING_MODE,  // Matches quoted strings
      hljs.NUMBER_MODE,  // Matches numbers
      {
        className: 'meta',
        begin: /@@@@@/,  // Matches custom delimiters or markers
        relevance: 10
      }
    ]
  };
});




let route = useRoute();
console.log(route.params.id)

const id = route.params.id || 'sap_commerce'; // Exemplo: você pode passar isso dinamicamente se necessário
const exams: Exam[] = examsData;

const exam = ref<Exam>({
  id: '',
  name: '',
  min_required: 0,
  max_questions: 0,
  questions: []
});

// Encontre o exame pelo id
const foundExam = exams.find(ex => ex.id === id);
if (foundExam) {
  exam.value = foundExam;
}

const checkQuestion = (question: Question) => {
  const questionIndex = selectedQuestions.value.findIndex(q => q.Question === question.Question);
  if (questionIndex === -1) return; // If question not found, return

  const userAnswers = isSingleAnswer(question)
      ? [selectedAnswer.value[questionIndex]]
      : selectedAnswers.value[questionIndex].map((answer, optionIndex) => answer ? optionIndex + 1 : -1).filter(optionIndex => optionIndex !== -1);

  const correctAnswers = question.CorrectAnswer.split(',').map(Number);

  if (arraysEqual(userAnswers, correctAnswers)) {
    alert("Question is correct")
  } else {
    alert("Question is incorrect")
  }
};

// Selecionar um número aleatório de perguntas e embaralhar
const selectedQuestions = ref<Question[]>([]);
const randomizeQuestions = () => {
  const availableQuestions = [...exam.value.questions];
  const maxQuestions = Math.min(exam.value.max_questions, availableQuestions.length);

  for (let i = 0; i < maxQuestions; i++) {
    const randomIndex = Math.floor(Math.random() * availableQuestions.length);
    selectedQuestions.value.push(availableQuestions.splice(randomIndex, 1)[0]);
  }
};
randomizeQuestions(); // Chamar a função para selecionar e embaralhar as perguntas

// Inicialize selectedAnswers com um objeto vazio para cada pergunta
const selectedAnswers = ref<boolean[][]>([]);
selectedQuestions.value.forEach((question, index) => {
  selectedAnswers.value[index] = new Array(question.Options.length).fill(false);
});

const selectedAnswer = ref<number[]>(new Array(selectedQuestions.value.length).fill(null));

const examCompleted = ref(false);
const passed = ref(false);

let finalScore = ref(0.0)

const submitExam = () => {
  let correctCount = 0;
  selectedQuestions.value.forEach((question, index) => {
    const userAnswers = isSingleAnswer(question) ? [selectedAnswer.value[index]] : selectedAnswers.value[index].map((answer, optionIndex) => answer ? optionIndex + 1 : -1).filter(optionIndex => optionIndex !== -1)
    const correctAnswers = question.CorrectAnswer.split(',').map(Number);

    if (arraysEqual(userAnswers, correctAnswers)) {
      correctCount++;
    }
  });

  const score = (correctCount / selectedQuestions.value.length) * 100;
  console.log(`Score: ${score}%`);

  finalScore.value = score

  passed.value = score >= exam.value.min_required;
  examCompleted.value = true;
};

const arraysEqual = (arr1: number[], arr2: number[]): boolean => {
  if (arr1.length !== arr2.length) return false;
  for (let i = 0; i < arr1.length; i++) {
    if (arr1[i] !== arr2[i]) return false;
  }
  return true;
};

const isSingleAnswer = (question: Question): boolean => {
  const correctAnswers = question.CorrectAnswer.split(',').map(Number);
  return correctAnswers.length === 1;
};

const isQuestionCorrect = (question: Question): boolean => {
  if (!examCompleted.value) return true; // Return true if exam is not completed
  const questionIndex = selectedQuestions.value.findIndex(q => q.Question === question.Question);
  const userAnswers = isSingleAnswer(question) ? [selectedAnswer.value[questionIndex]] : selectedAnswers.value[questionIndex].map((answer, optionIndex) => answer ? optionIndex + 1 : -1).filter(optionIndex => optionIndex !== -1)
  const correctAnswers = question.CorrectAnswer.split(',').map(Number);
  return arraysEqual(userAnswers, correctAnswers);
};

const questionHasInteraction = (questionIndex: number): boolean => {
  return selectedAnswer.value[questionIndex] !== null || selectedAnswers.value[questionIndex].some(answer => answer);
};

const updateInteraction = (questionIndex: number) => {
  // Reset red border when user interacts with the question
  const question = selectedQuestions.value[questionIndex];
  if (!isQuestionCorrect(question)) {
    // Ensure red border only when the answer is incorrect
    const cardElement = document.getElementById(`card-${questionIndex}`);
    if (cardElement) {
      cardElement.classList.remove('border-danger');
      // Force reflow to trigger CSS transition
      void cardElement.offsetWidth;
      cardElement.classList.add('border-danger');
    }
  }
};
</script>

<style>
.card {
  margin-bottom: 20px;
  transition: border-color 0.3s ease;
}
.border-danger {
  border-color: red !important;
}
</style>
