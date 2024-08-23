<template>
  <div>
    <section class="container">

      <p class="breadcrumbs"><a href="/" class="interpreter">Главная</a> > О нас</p>

      <h1>О нас</h1>

      <div class="aboutUs">
        <div>
          <p class="textAboutUs">Добро пожаловать в наш SERVICE CENTER! Мы - команда опытных специалистов, готовых
            сделать ваше общение с техникой простым, удобным и безопасным.</p>
          <p class="textAboutUs">Наш магазин предлагает широкий ассортимент качественной техники от ведущих мировых
            производителей. Мы гордимся предоставляемым выбором смартфонов, ноутбуков, планшетов,
            игровых консолей и другой электроники, которая удовлетворит самые взыскательные потребности.</p>
          <p class="textAboutUs">В нашем сервис-центре ваша техника — в надежных руках.
            Наши опытные специалисты помогут с обслуживанием, ремонтом и настройкой.</p>
          <p class="textAboutUs">
            Присоединяйтесь к нашему сообществу, мы ценим ваше доверие и готовы обеспечить приятное и беззаботное
            общение с вашей техникой!</p>
          <p class="textAboutUs">Спасибо, что выбрали SERVICE CENTER. Мы всегда готовы помочь вам!</p>

        </div>

        <img src="../assets/images/master2.webp" alt="Мастер">

      </div>

      <h1 class="heading">График работы</h1>

      <p class="textAboutUs">
        Мы работаем для вас без выходных и перерывов с 9 утра до 6 вечера. Наша команда старается обеспечить вас
        высококачественным обслуживанием и поддержкой в удобное для вас время. Ждем вас в любой день недели, чтобы
        помочь вам с выбором, покупкой или ремонтом вашей техники. Не стесняйтесь обращаться к нам в любое время
        рабочего
        дня - мы здесь, чтобы помочь вам!
      </p>

      <h1 class="heading">Наш персонал</h1>

      <div class="staff">

        <div class="row">
          <div v-for="employee in employees" :key="employee.id" class="col-lg-3 col-md-3 col-sm-4">
            <div class="card">

              <img v-if='employee.photo' :src='employee.photo' class="card-img-top img-fluid custom-img"
                alt="Сотрудник">
              <img v-else src='../assets/images/account-no-image.png' class="card-img-top img-fluid custom-img"
                alt="Сотрудник">
              <div class="card-body">
                <h5>{{ employee.user.first_name }} {{ employee.user.last_name }}</h5>
                <p class="textName">{{ employee.position }}</p>
                <p> Опыт работы: <span class='age-count'>{{ employee.experience_years }}</span> </p>
              </div>
            </div>
          </div>
        </div>

      </div>

      <h1 class="heading">Наши партнёры</h1>

      <p class="textAboutUs">Мы гордимся нашими партнерскими отношениями с ведущими мировыми брендами в
        сфере электроники. Наша компания тесно сотрудничает с такими индустриальными гигантами, как Apple,
        Samsung, Microsoft, LG и Sony. Эти компании являются символами инновации, качества и надежности в мире
        технологий, и мы гордимся возможностью работать с ними.</p>
      <p class="textAboutUs">Наше партнерство позволяет нам предлагать нашим клиентам широкий ассортимент качественной
        электроники,
        включая последние модели смартфонов, ноутбуков, телевизоров, игровых консолей и многого другого. Мы стремимся к
        тому,
        чтобы наши клиенты всегда имели доступ к самым передовым технологиям и наилучшим продуктам на рынке.</p>
      <p class="textAboutUs">Благодаря нашим партнерам мы можем обеспечить нашим клиентам лучшие условия покупки,
        первоклассное
        обслуживание и гарантию качества. Мы благодарим наших партнеров за долгосрочное сотрудничество и возможность
        делиться
        с нашими клиентами лучшими технологическими решениями.</p>
      <callModal>
      </callModal>
    </section>
  </div>
</template>
<script>
import callModal from '@/components/sendCallModal.vue';
import { getEmployees } from '@/api/employees-list'
export default {
  name: "aboutView",
  components: { callModal },
  data() {
    return {
      employees: []
    }
  },
  methods: {
    declination(number, titles) {
      const cases = [2, 0, 1, 1, 1, 2];
      return titles[(number % 100 > 4 && number % 100 < 20) ? 2 : cases[(number % 10 < 5) ? number % 10 : 5]];
    },
    age_decline_print() {
      const elements = document.querySelectorAll('.age-count')
      console.log(elements)
      elements.forEach(function (el) {
        const count = el.textContent
        const title = this.declination(count, [' год', ' года', ' лет'])
        console.log(title)
        const age = count + title
        el.textContent = age
      })
    }
  },
  async created() {
    this.employees = await getEmployees()
    this.employees.forEach(employee => {
      const count = employee.experience_years
      const title = this.declination(count, [' год', ' года', ' лет'])
      employee.experience_years += title
      console.log(this.employees)
    })
  },
mounted() {
  this.age_decline_print()
}
}
</script>
<style scoped>
.interpreter,
.breadcrumbs {
  color: rgb(127, 127, 127);
  text-decoration: none;
}

.interpreter:hover {
  text-decoration: underline;
}

.aboutUs p,
.textAboutUs {
  text-align: justify;
}

.aboutUs {
  display: flex;
}

.heading {
  margin: 16px 0;
  text-align: center;
}

.textName {
  margin: 0;
}

.card {
  margin-bottom: 16px;
}
.card-body{
  height: 130px;
}
.custom-img {
  object-fit: cover;
  height: 300px;
}


@media (max-width: 993px) {
  section {
    padding-top: 116px;
  }
  .card-body{
  height: auto;
}
}

@media (min-width: 992px) {

  .menu {
    width: 100%;
    position: fixed;
    z-index: 10;
  }

  .aboutUs div {
    width: 60% !important;
    margin-right: 16px !important;
  }

  .aboutUs img {
    height: 100% !important;
    margin: 0 !important;
  }

  .aboutUs {
    flex-direction: row !important;
    align-items: center;
    justify-content: space-between;
  }

  .map {
    height: 500px;
    width: 500px;
  }

}

@media (max-width: 992px) {

  header {
    margin-bottom: 16px;
  }

  .interpreter {
    margin-top: 16px;
  }

  .dropdown-item {
    color: white !important;
  }

  .dropdown-menu {
    background-color: #0d6efd !important;
    border: none !important;
  }

  .menu {
    position: relative;
  }

  .aboutUs {
    flex-direction: column;
  }

  .aboutUs div {
    width: 100%;
  }

  .aboutUs img {
    margin: 0 10%;
  }

  .map {
    height: 300px;
    width: 300px;
  }
  .col-sm-4 {
    flex: 0 0 auto;
    width: 49.33333333%;
  }
}

@media (max-width: 768px) {

  .contacts {
    flex-direction: column;
  }

  .contacts .map {
    margin-top: 16px;
  }

  .btn {
    width: 100%;
  }

  .container {
    flex-direction: column-reverse;
  }

  .map {
    margin-bottom: 16px;
    width: 100%;
  }
}

@media (min-width: 768px) {

  .modal-body {
    display: flex;
    flex-direction: column;
  }
}

@media (max-width: 576px) {

  .btn {
    width: 100%;
  }
}

</style>