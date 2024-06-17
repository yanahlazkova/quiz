<template>
  <div class="app-body">
    <section class="container">
      <div class="questionBox" id="app">
        <transition :duration="{ enter: 500, leave: 300 }" enter-active-class="animated zoomIn"
          leave-active-class="animated zoomOut" mode="out-in">
          <div v-if="questionIndex < quiz.questions.length" :key="questionIndex">
            <header>
              <h1 class="title is-6">VueQuiz</h1>
              <div class="progressContainer">
                <progress class="progress is-info is-small" :value="(questionIndex / quiz.questions.length) * 100"
                  max="100">{{ (questionIndex / quiz.questions.length) * 100 }}%</progress>
                <p>{{ (questionIndex / quiz.questions.length) * 100 }}% complete</p>
              </div>
            </header>

            <h2 class="titleContainer title">{{ quiz.questions[questionIndex].text }}</h2>

            <div class="optionContainer">
              <div class="option" v-for="(response, index) in quiz.questions[questionIndex].responses"
                @click="selectOption(index)" :class="{ 'is-selected': userResponses[questionIndex] === index }"
                :key="index">
                {{ charIndex(index) }}. {{ response.text }}
              </div>
            </div>

            <footer class="questionFooter">
              <nav class="pagination" role="navigation" aria-label="pagination">
                <a class="button" @click="prev" :disabled="questionIndex < 1">Back</a>
                <a class="button" :class="userResponses[questionIndex] === null ? '' : 'is-active'" @click="next"
                  :disabled="questionIndex >= quiz.questions.length">{{ userResponses[questionIndex] === null ? 'Skip' :
                    'Next' }}</a>
              </nav>
            </footer>
          </div>
        </transition>
        <transition :duration="{ enter: 500, leave: 300 }" enter-active-class="animated zoomIn"
          leave-active-class="animated zoomOut" mode="out-in">
          <div v-if="questionIndex >= quiz.questions.length" :key="questionIndex"
            class="quizCompleted has-text-centered">
            <span class="icon">
              <i class="fa" :class="score() > 3 ? 'fa-check-circle-o is-active' : 'fa-times-circle'"></i>
            </span>
            <h2 class="title">
              You did {{ score() > 7 ? 'an amazing' : score() < 4 ? 'a poor' : 'a good' }} job! </h2>
                <p class="subtitle">Total score: {{ score() }} / {{ quiz.questions.length }}</p>
                <br />
                <a class="button" @click="restart()">restart <i class="fa fa-refresh"></i></a>
          </div>
        </transition>
      </div>
    </section>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';

const ServerUrl = 'http://127.0.0.1:8000';

// Асинхронная функция для получения вопросов с сервера
async function getQuestions() {
  const url = `${ServerUrl}/questions`;
  const response = await fetch(url);
  const data = await response.json();
  console.log(data);
  // Обработка полученных данных
  const formattedQuestions = data.map((question) => ({
    text: question.text,
    responses: Object.entries(question.answers).map(([answerKey, answerText]) => ({
      text: answerText,
      correct: false, // Логика для определения правильного ответа на основе answerKey (если имеется)
    })),
  }));
  console.log(formattedQuestions);
  return formattedQuestions;
}

// Реактивные переменные для хранения данных и состояния викторины
const questions = ref([]);
const quiz = ref({
  user: "Dave",
  questions: [],
});
const questionIndex = ref(0);
const userResponses = ref([]);

// Получение вопросов при монтировании компонента
onMounted(async () => {
  questions.value = await getQuestions();
  quiz.value.questions = questions.value;
  userResponses.value = Array(quiz.value.questions.length).fill(null);
});

const restart = () => {
  questionIndex.value = 0;
  userResponses.value = Array(quiz.value.questions.length).fill(null);
};

const selectOption = (index: number) => {
  userResponses.value[questionIndex.value] = index;
};

const next = () => {
  if (questionIndex.value < quiz.value.questions.length - 1) {
    questionIndex.value++;
  }
};

const prev = () => {
  if (questionIndex.value > 0) {
    questionIndex.value--;
  }
};

const score = () => {
  let score = 0;
  for (let i = 0; i < userResponses.value.length; i++) {
    if (
      typeof quiz.value.questions[i].responses[userResponses.value[i]] !== 'undefined' &&
      quiz.value.questions[i].responses[userResponses.value[i]].correct
    ) {
      score++;
    }
  }
  return score;
};

const charIndex = (i: number) => {
  return String.fromCharCode(97 + i);
};
</script>


<style lang="scss" scoped>
$trans_duration: 0.3s;
$primary_color: #3d5afe;


.app-body {
  font-family: 'Open Sans', sans-serif;
  font-size: 16px;
  height: 100vh;
  background: #cfd8dc;
  cursor: default !important;
  user-select: none;
  display: flex;
  align-items: center;
  justify-content: center;
}

.button {
  transition: $trans_duration;
}

.title,
.subtitle {
  font-family: Montserrat, sans-serif;
  font-weight: normal;
}

.animated {
  transition-duration: calc($trans_duration / 2);
}

.container {
  margin: 0 0.5rem;
  width: 30rem;
}

.questionBox {
  flex-grow: 1;
  width: 100%;
  flex-grow: 1;
  min-height: 30rem;
  background: #FAFAFA;
  border-radius: 0.5rem;
  overflow: hidden;
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.19), 0 6px 6px rgba(0, 0, 0, 0.23);
}

header {
  width: 100%;
  background: rgba(0, 0, 0, 0.025);
  padding: 1.5rem;
  text-align: center;
  border-bottom: 1px solid rgba(0, 0, 0, 0.1);

  h1 {
    font-weight: bold;
    margin-bottom: 1rem !important;
  }

  .progressContainer {
    width: 60%;
    margin: 0 auto;

    >progress {
      margin: 0;
      border-radius: 5rem;
      overflow: hidden;
      border: none;

      color: $primary_color;

      &::-moz-progress-bar {
        background: $primary_color;
      }

      &::-webkit-progress-value {
        background: $primary_color;
      }
    }

    >p {
      margin: 0;
      margin-top: 0.5rem;
    }
  }
}

.titleContainer {
  text-align: center;
  margin: 0 auto;
  padding: 1.5rem;

}

.quizForm {
  display: block;
  white-space: normal;

  height: 100%;
  width: 100%;

  .quizFormContainer {
    height: 100%;
    margin: 15px 18px;

    .field-label {
      text-align: left;
      margin-bottom: 0.5rem;
    }
  }
}

.quizCompleted {
  width: 100%;
  padding: 1rem;
  text-align: center;

  >.icon {
    color: #FF5252;
    font-size: 5rem;

    .is-active {
      color: #00E676;
    }
  }
}

.questionContainer {
  white-space: normal;

  height: 100%;
  width: 100%;

}

.optionContainer {
  padding: 1rem 0;

  .option {
    border-radius: 290486px;
    padding: 9px 18px;
    margin: 0 18px;
    margin-bottom: 12px;
    transition: $trans_duration;
    cursor: pointer;
    background-color: rgba(0, 0, 0, 0.05);
    color: rgba(0, 0, 0, 0.85);
    border: transparent 1px solid;

    &.is-selected {
      border-color: rgba(black, 0.25);
      background-color: white;
    }

    &:hover {
      background-color: rgba(0, 0, 0, 0.1);
    }

    &:active {
      transform: scaleX(0.9);
    }
  }
}

.questionFooter {
  background: rgba(0, 0, 0, 0.025);
  border-top: 1px solid rgba(0, 0, 0, 0.1);
  width: 100%;
  
  .pagination {
    padding: 1rem;
  }
}

.pagination {
  display: flex;
  justify-content: space-between;
}

.button {
  padding: 0.5rem 1rem;
  border: 1px solid rgba(0, 0, 0, 0.25);
  border-radius: 5rem;
  margin: 0 0.25rem;

  transition: 0.3s;

  &:hover {
    cursor: pointer;
    background: #ECEFF1;
    border-color: rgba(0, 0, 0, 0.25);
  }

  &.is-active {
    background: $primary_color;
    color: white;
    border-color: transparent;

    &:hover {
      background: darken($primary_color, 10%);

    }
  }
}

@media screen and (min-width: 769px) {
  .questionBox {
    align-items: center;
    justify-content: center;

    .questionContainer {
      display: flex;
      flex-direction: column;
    }
  }
}

@media screen and (max-width: 768px) {
  .sidebar {
    height: auto !important;
    border-radius: 6px 6px 0px 0px;
  }
}
</style>
