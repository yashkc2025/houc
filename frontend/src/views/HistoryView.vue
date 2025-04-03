<script setup>
import server from "@/assets/server";
import SelectComponent from "@/components/SelectComponent.vue";
import TextAreaComponent from "@/components/TextAreaComponent.vue";
import { fetchData, postData } from "@/fx/api";
import AppLayout from "@/layouts/AppLayout.vue";
import { IconEyeOff } from "@tabler/icons-vue";
import { IconSquareRoundedXFilled } from "@tabler/icons-vue";
import { IconAlignBoxLeftMiddle } from "@tabler/icons-vue";
import { IconCarambola } from "@tabler/icons-vue";
import { IconClockFilled } from "@tabler/icons-vue";
import { IconCircleCheckFilled } from "@tabler/icons-vue";
import { onMounted, ref, watch } from "vue";

const labels = ["Service", "Price", "Professional Name", "Contact", "Status"];

const ratingOptions = [
  {
    id: 1,
    name: "⭐",
  },
  {
    id: 2,
    name: "⭐⭐",
  },
  {
    id: 3,
    name: "⭐⭐⭐",
  },
  {
    id: 4,
    name: "⭐⭐⭐⭐",
  },
  {
    id: 5,
    name: "⭐⭐⭐⭐⭐",
  },
];
const history = ref([]);

onMounted(async () => {
  const data = await fetchData(server.service.history);
  history.value = data.map((a) => {
    return {
      id: a.id,
      name: a.service.name,
      price: a.service.price,
      professional: a.service_professional.name,
      phone: a.service_professional.phone,
      status: a.request_status,
    };
  });
  console.log(history.value);
});

let review = ref("");
let rating = ref("");
let request_id = ref();

function selectRequest(id) {
  const modal = document.getElementById("modal");
  modal.style.display = "flex";
  request_id.value = id;
}

async function closeRequest() {
  await postData(server.service.close_request, {
    request_id: request_id.value,
    rating: rating.value,
    review_text: review.value,
  });
}

watch(rating, (x) => {
  console.log(x);
});
</script>

<template>
  <AppLayout msg="View your past bookings !">
    <div class="app-body">
      <table>
        <thead>
          <tr>
            <th v-for="l in labels" :key="l">{{ l }}</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="r in history" :key="r.id">
            <td>{{ r.name }}</td>
            <td>{{ "₹" + r.price }}</td>
            <td>{{ r.professional }}</td>
            <td>{{ r.phone }}</td>
            <!-- <td class="rating">
            <span v-for="n in r.ratings" :key="n">
              <IconCarambolaFilled class="icon star" />
            </span>
          </td> -->
            <td>
              <div class="status">
                <IconCircleCheckFilled
                  class="completed"
                  v-if="r.status === 'complete'"
                />
                <IconEyeOff
                  class="pending"
                  v-if="r.status === 'requested'"
                  @click="selectRequest(r.id)"
                />
                <IconClockFilled
                  class="pending"
                  v-if="r.status === 'accepted'"
                  @click="selectRequest(r.id)"
                />
                <IconSquareRoundedXFilled
                  class="cancelled"
                  v-if="r.status === 'rejected'"
                />
              </div>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <div class="modal" id="modal">
      <h1>Close Request</h1>
      <SelectComponent
        label="Rating"
        name="rating"
        :options="ratingOptions"
        v-model="rating"
      >
        <IconCarambola />
      </SelectComponent>
      <TextAreaComponent
        label="Review"
        name="review_text"
        placeholder="Any feedbacks you have ?"
        v-model="review"
      >
        <IconAlignBoxLeftMiddle />
      </TextAreaComponent>
      <button class="styled-button" @click="closeRequest()">
        Mark as completed
      </button>
    </div>
  </AppLayout>
</template>

<style scoped>
h1 {
  text-align: center;
}
th:first-child,
td:first-child {
  width: 35%; /* Adjust based on your needs */
}
th:nth-child(2),
td:nth-child(2) {
  width: 10%; /* Adjust based on your needs */
}
.app-body {
  position: relative;
}
.modal {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 60vw;
  /* height: 60vh; */
  background-color: var(--accent-100);
  border-radius: var(--size-sm);
  display: none;
  flex-direction: column;
  gap: var(--size-lg);
  padding: var(--size-md);
}

.completed {
  filter: invert(16%) sepia(53%) saturate(6429%) hue-rotate(156deg)
    brightness(111%) contrast(80%);
}

.cancelled {
  filter: invert(12%) sepia(61%) saturate(6120%) hue-rotate(337deg)
    brightness(96%) contrast(94%);
}

.pending {
  filter: invert(72%) sepia(76%) saturate(2414%) hue-rotate(6deg)
    brightness(102%) contrast(94%);
}
</style>
