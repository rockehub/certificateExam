<script setup lang="ts">

import VueMarkdown from "vue-markdown-render";
import VCodeBlock from "@wdns/vue-code-block";
import type {Alternative, Exam, PromptFinal, Question} from "~/types";
import {ref} from "vue";
import axios from "axios";
import hljs from "highlight.js/lib/core";


const props = defineProps<{question: Question, exam: Exam, examCompleted: boolean, isImmersive:boolean}>()

const emit = defineEmits(['isCorrectQuestion'])

const selectedCheckboxAnswer = ref<{[key: number]: boolean}[]>([]);
const selectedAnswer = ref<Alternative[]>([]);
const loadingExplanation = ref<boolean>(false);
const promptExplanation = ref<{explanation: string}>( {explanation: "" } );

const cardBoard = ref();

const isQuestionCorrect = (question: Question): boolean => {
  const correctAnswers = question.CorrectAnswer.split(',').map((item)=> {
    return question.Options.find((option) => option.number === Number(item));
  });
  return arraysEqual(selectedAnswer.value, correctAnswers);
};


const isSingleAnswer = (question: Question): boolean => {
  return question.CorrectAnswer.split(',').map(Number).length === 1;
};
const arraysEqual = (arr1: Alternative[], arr2: (Alternative | undefined)[]): boolean => {
  if (arr1.length !== arr2.length) return false;

  const sortedArr1 = arr1.map(a => a.number).sort((a, b) => a - b);
  const sortedArr2 = arr2.map(a => a?.number).filter(n => n !== undefined).sort((a, b) => a - b);

  return sortedArr1.every((num, index) => num === sortedArr2[index]);
};


const checkQuestion = (question: Question) => {
  if (isQuestionCorrect(question)) {
    alert("Correct")
  } else {
    alert("incorrect")
  }
};



const promptReason = async (isWrong: boolean = false) => {
  loadingExplanation.value = true

  if (props.exam === null) {
    throw new Error("no exam")
  }


  const questionId = `${props.exam.id}-${props.question.Question}`;

  // Criar uma string com todas as opções da questão
  const optionsText = props.question.Options.map((option, index) => `Option ${index + 1}: ${option.question}`).join('\n');

  // Incluir as opções no prompt
  let promptText = `in ${props.exam.name} context Provide a detailed explanation of the answer to the following question: '${props.question.QuestionText}', along with a practical example. The options for this question are:\n${optionsText} are (${props.question.CorrectAnswer.split(',').length} correct) `;

  if (isWrong) {
    promptText += ` correct answer: ${props.question.CorrectAnswer}`
  }


  try {
    // Verificar se já existe uma explicação salva
    const savedExplanation = await $fetch<{
      explanation: string | null
    }>(`/api/getExplanation?questionId=${questionId}`);

    if (savedExplanation.explanation) {
      // Se houver explicação salva, exibe
      promptExplanation.value = {explanation: savedExplanation.explanation};

      return;
    }

    // Caso não exista explicação salva, chama a API do Gemini para pegar a explicação e o exemplo
    const response = await axios.post(`https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-pro:generateContent?key=${import.meta.env.VITE_GEMINI_API_KEY}`, {
      contents: [{
        parts: [{text: promptText}]
      }]
    });

    // Extrair explicações e exemplos da resposta
    const content: PromptFinal = response.data;
    const explanationParts = content.candidates?.[0].content.parts;
    const explanation = explanationParts?.[0]?.text || 'No explanation provided.';

    // Atualizar a explicação na interface
    promptExplanation.value = {explanation};

  } catch (error) {
    console.error('Error fetching explanation:', error);
  } finally {
    loadingExplanation.value = false
  }
};


const rateAnswer = async (isCorrect: boolean) => {

  if (props.exam === null) {
    throw new Error("no exam")
  }

  if (isCorrect) {
    let {explanation} = promptExplanation.value;
    let questionId = `${props.exam.id}-${props.question.Question}`;
    await $fetch('/api/saveExplanation', {
      method: 'POST',
      body: {questionId, explanation}
    });

  } else {
    console.log('Resposta incorreta, tentando novamente...');
    await promptReason(true);
  }
};


const updateInteraction = () => {
  const cardElement = cardBoard.value
  if (!isQuestionCorrect(props.question)) {

    if (cardElement && props.examCompleted) {
      cardElement.classList.remove('border-danger');
      void cardElement.offsetWidth;
      cardElement.classList.add('border-danger');
    }
  }else{
    cardElement.classList.remove('border-danger');
  }

  emit("isCorrectQuestion", [props.question.Question, isQuestionCorrect(props.question)])

};

const pushQuestion = () => {
  selectedCheckboxAnswer.value.forEach((isSelected, key) => {
    const alternative = props.question.Options.find(opt => opt.number === key);
    if (alternative) {
      if (isSelected) {
        if (!selectedAnswer.value.some(opt => opt.number === key)) {
          selectedAnswer.value.push(alternative);
        }
      } else {

        selectedAnswer.value = selectedAnswer.value.filter(opt => opt.number !== key);
      }
    }
  });

  console.log(selectedAnswer.value);
  updateInteraction()
};




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
        begin: /@@@@@/, // Matches custom delimiters or markers
        relevance: 10
      }
    ]
  };
});

const STORAGE_KEY = `exam-${props.exam.id}-question-${props.question.Question}-${props.isImmersive ? 'immersive' : 'normal'}`;

// Função para salvar progresso no localStorage
const saveProgress = () => {
  const progressData = {
    selectedCheckboxAnswer: selectedCheckboxAnswer.value,
    selectedAnswer: selectedAnswer.value,
  };
  localStorage.setItem(STORAGE_KEY, JSON.stringify(progressData));
};

// Função para carregar progresso do localStorage
const loadProgress = () => {
  const savedData = localStorage.getItem(STORAGE_KEY);
  if (savedData) {
    const parsedData = JSON.parse(savedData);
    selectedCheckboxAnswer.value = parsedData.selectedCheckboxAnswer || [];
    selectedAnswer.value = parsedData.selectedAnswer || [];
  }
  updateInteraction()
};

// Função para limpar progresso do localStorage (caso necessário)
const clearProgress = () => {
  localStorage.removeItem(STORAGE_KEY);
  selectedCheckboxAnswer.value = [];
  selectedAnswer.value = [];
};

onMounted(loadProgress);


// Atualiza o localStorage sempre que o usuário seleciona uma resposta
watch([selectedAnswer, selectedCheckboxAnswer], saveProgress, { deep: true });


</script>

<template>
  <div ref="cardBoard" class="card">
      <div class="card-header">
        <div class="d-flex justify-content-between">
          <div style="max-width: 80%">
            <h5>N{{ question.Question }}</h5>
            <h4>{{ question.QuestionText }} {{ question.CorrectAnswer.split(',').length }}</h4>
          </div>
          <div>
            <div class="d-flex justify-content-end gap-2">
              <button @click="checkQuestion(question)" class="btn btn-primary" v-if="!isImmersive"> check question</button>
              <button @click="promptReason()" class="btn btn-secondary" v-if="!isImmersive">Why?</button>

            </div>
          </div>

        </div>
        <VCodeBlock v-if="question.Code" highlightjs :code="question.Content" :lang="question.Lang"
                    theme="github-dark-dimmed"/>


      </div>
      <div class="card-body">
        <div v-if="isSingleAnswer(question)">
          <div v-for="(option, optionIndex) in question.Options" :key="optionIndex" class="form-check">
            <input type="radio"
                   class="form-check-input"
                   :id="`${question.Question}-${option.number}`"
                   :value="option"
                   v-model="selectedAnswer[0]"
                   @change="updateInteraction"
            >
            <label class="form-check-label" :for="`${question.Question}-${option.number}`">{{ option.question }}</label>
          </div>
        </div>
        <div v-else>
          <div v-for="(option, optionIndex) in question.Options" :key="optionIndex" class="form-check">
            <input type="checkbox"
                   class="form-check-input"
                   :id="`${question.Question}-${option.number}`"
                   :value="option.number"
                   v-model="selectedCheckboxAnswer[option.number]"
                   @change="pushQuestion"
            >
            <label class="form-check-label" :for="`${question.Question}-${option.number}`">{{ option.question }}</label>
          </div>
        </div>


        <div v-if="promptExplanation.explanation.length > 0 && !isImmersive" class="card-body">
          <vue-markdown :source="promptExplanation.explanation"/>
          <div class="d-flex gap-2">
            <button @click="rateAnswer(true)" class="btn btn-success">OK</button>
            <button @click="rateAnswer(false)" class="btn btn-danger">NOT OK</button>
          </div>
        </div>
        <div class="" v-if="loadingExplanation"> searching</div>

      </div>
  </div>

</template>

<style scoped>

</style>