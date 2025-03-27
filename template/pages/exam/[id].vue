<template>
  <div class="container mb-50">
    <h1 v-if="exam">{{ exam.name }} Exam</h1>
    <div v-if="!exam || (exam && exam.questions.length === 0)" class="alert alert-warning">
      No questions found for this exam.
    </div>

    <question-cards v-for="(question, questionIndex) in selectedQuestions" :key="questionIndex" :question="question"
                    :exam="exam" :exam-completed="examCompleted"
                    @isCorrectQuestion="pushToResult"
    />

    <div class="d-flex gap-2 justify-content-center">
      <button class="btn btn-primary mt-3" @click="submitExam">Finish Exam</button>
      <button class="btn btn-danger mt-3" @click="clearProgress">Clear Progress</button>
      <button class="btn btn-info mt-3" @click="showQuestionLoader = !showQuestionLoader">Load Questions by numbers
      </button>
      <NuxtLink to="/" class="btn btn-secondary mt-3">Back To List</NuxtLink>
    </div>
    <div class="row mt-2" v-if="showQuestionLoader">
      <div class="input-group ">
        <input type="text" class="form-control" v-model="questionsToLoad">
        <button class="btn btn-info" @click="loadSpecificQuestions">Load</button>
      </div>
    </div>
    <div v-if="examCompleted" class="mt-3 text-center">
      <h3 v-if="passed" class="alert alert-success">Congratulations! You passed the exam. {{ finalScore }}</h3>
      <h3 v-else class="alert alert-danger">Sorry, you did not pass the exam. {{ finalScore }}</h3>
    </div>
  </div>
</template>

<script lang="ts" setup>
import {ref} from 'vue';
import type {Exam, Question} from '@/types'; // Defina seus tipos TypeScript


const route = useRoute();


const id = route.params.id || 'sap_commerce';

const exam = ref<Exam>({
  id: '',
  name: '',
  min_required: 0,
  max_questions: 0,
  questions: []
});

exam.value = await $fetch<Exam>(`/api/getExam?examId=${id}`)


const selectedQuestions = ref<Question[]>([]);
const completeQuestions = ref<{ questionNumber: string, isCorrect: boolean }[]>([])
const examCompleted = ref(false);
const passed = ref(false);
const finalScore = ref(0);
const questionsToLoad = ref<string>('')
const showQuestionLoader = ref(false)


const STORAGE_KEY = `exam-progress-${id}`;

const saveProgress = () => {
  const progress = {
    selectedQuestions: selectedQuestions.value,
  };
  localStorage.setItem(STORAGE_KEY, JSON.stringify(progress));
};


const loadProgress = () => {
  const savedProgress = localStorage.getItem(STORAGE_KEY);
  if (savedProgress) {
    const progress = JSON.parse(savedProgress);
    console.log(progress)
    selectedQuestions.value = progress.selectedQuestions;
  } else {
    randomizeQuestions();
  }
};


const clearProgress = () => {
  localStorage.removeItem(STORAGE_KEY);
  location.reload();
};

const loadSpecificQuestions = () => {

  if (exam.value === null) {
    throw new Error("no exam")
  }
  try {
    if (questionsToLoad.value.length > 0) {

      const availableQuestions = [...exam.value.questions];
      let questionNumbers: string[] = questionsToLoad.value.split(',')

      if (questionNumbers.length > 0) {
        selectedQuestions.value = availableQuestions.filter((q) => questionNumbers.includes(q.Question))
      }
    }
  } catch (e) {
    alert(e)
  }
}

const randomizeQuestions = () => {

  if (exam.value === null) {
    throw new Error("no exam")
  }
  const availableQuestions = [...exam.value.questions];
  const maxQuestions = Math.min(exam.value.max_questions, availableQuestions.length);

  selectedQuestions.value = [];
  for (let i = 0; i < maxQuestions; i++) {
    const randomIndex = Math.floor(Math.random() * availableQuestions.length);
    selectedQuestions.value.push(availableQuestions.splice(randomIndex, 1)[0]);
  }

};


const pushToResult = ([questionNumber, isCorrect]: [string, boolean]) => {
  const index = completeQuestions.value.findIndex(q => q.questionNumber === questionNumber);
  if (index !== -1) {
    completeQuestions.value[index].isCorrect = isCorrect;
  } else {
    completeQuestions.value.push({ questionNumber, isCorrect });
  }
  saveProgress()
};

const countCorrectAnswers = (): number => {
  return completeQuestions.value.filter(q => q.isCorrect).length;
};

const submitExam = () => {

  if (exam.value === null) {
    throw new Error("no exam")
  }
  const totalQuestions = selectedQuestions.value.length;

  let correctCount = countCorrectAnswers()

  const finalScoreA = (correctCount / totalQuestions) * 100;


  const minRequiredPercentage = (exam.value.min_required / totalQuestions) * 100;


  const passedA = finalScoreA >= minRequiredPercentage;


  finalScore.value = finalScoreA;
  passed.value = passedA;
  examCompleted.value = true;
};

onMounted(loadProgress);


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
