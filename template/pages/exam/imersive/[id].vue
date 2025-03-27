<template>
  <div class="container mb-50">
    <div class="text-center mt-50">
      <h1 v-if="exam">{{ exam.name }} Exam</h1>
    </div>
    <div v-if="!exam || (exam && exam.questions.length === 0)" class="alert alert-warning">
      No questions found for this exam.
    </div>

    <div v-if="!examCompleted" class="mt-100">
      <question-cards
          v-if="selectedQuestions[currentQuestionIndex]"
          :question="selectedQuestions[currentQuestionIndex]"
          :exam="exam"
          :exam-completed="examCompleted"
          @isCorrectQuestion="pushToResult"
          :is-immersive="true"
      />

      <div class="d-flex gap-2 justify-content-center mt-3">
        <button class="btn btn-secondary" @click="prevQuestion" :disabled="currentQuestionIndex === 0">
          Previous
        </button>
        <button class="btn btn-primary" @click="nextQuestion"
                v-if="currentQuestionIndex < selectedQuestions.length - 1">
          Next
        </button>
        <button class="btn btn-success" @click="submitExam"
                v-if="currentQuestionIndex === selectedQuestions.length - 1">
          Finish Exam
        </button>
      </div>
    </div>

    <div class="row mt-2" v-if="showQuestionLoader">
      <div class="input-group">
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
import {ref, computed, onMounted} from 'vue';
import type {Exam, Question} from '@/types';

const route = useRoute();
const id = route.params.id || 'sap_commerce';
const exam = ref<Exam>({id: '', name: '', min_required: 0, max_questions: 0, questions: []});
exam.value = await $fetch<Exam>(`/api/getExam?examId=${id}`);

const selectedQuestions = ref<Question[]>([]);
const completeQuestions = ref<{ questionNumber: string, isCorrect: boolean }[]>([]);
const currentQuestionIndex = ref(0);
const examCompleted = ref(false);
const passed = ref(false);
const finalScore = ref(0);
const questionsToLoad = ref<string>('');
const showQuestionLoader = ref(false);

const STORAGE_KEY = `exam-emersive-progress-${id}`;

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
  if (!exam.value) throw new Error("no exam");
  try {
    if (questionsToLoad.value.length > 0) {
      const availableQuestions = [...exam.value.questions];
      let questionNumbers: string[] = questionsToLoad.value.split(',');
      if (questionNumbers.length > 0) {
        selectedQuestions.value = availableQuestions.filter((q) => questionNumbers.includes(q.Question));
      }
    }
  } catch (e) {
    alert(e);
  }
};

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
    completeQuestions.value.push({questionNumber, isCorrect});
  }
  saveProgress();
};

const nextQuestion = () => {
  if (currentQuestionIndex.value < selectedQuestions.value.length - 1) {
    currentQuestionIndex.value++;
  }
};

const prevQuestion = () => {
  if (currentQuestionIndex.value > 0) {
    currentQuestionIndex.value--;
  }
};

const countCorrectAnswers = (): number => completeQuestions.value.filter(q => q.isCorrect).length;

const submitExam = () => {
  const totalQuestions = selectedQuestions.value.length;
  const correctCount = countCorrectAnswers();
  finalScore.value = (correctCount / totalQuestions) * 100;
  passed.value = finalScore.value >= (exam.value.min_required / totalQuestions) * 100;
  examCompleted.value = true;
};

onMounted(() => {
  loadProgress()
  document.addEventListener("click", requestFullScreen, {once: true}); // Trigger on first click
});


const requestFullScreen = () => {
  const elem = document.documentElement;

  if (elem.requestFullscreen) {
    elem.requestFullscreen();
  } else if (elem.mozRequestFullScreen) { // Firefox
    elem.mozRequestFullScreen();
  } else if (elem.webkitRequestFullscreen) { // Chrome, Safari, and Opera
    elem.webkitRequestFullscreen();
  } else if (elem.msRequestFullscreen) { // IE/Edge
    elem.msRequestFullscreen();
  }
};

</script>

<style>
.card {
  margin-bottom: 20px;
  transition: border-color 0.3s ease;
}
</style>
