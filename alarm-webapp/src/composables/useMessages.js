import { ref } from "vue";

export default function useMessages() {
  let messageNextId = 0;
  const messages = ref([]);

  function showMessage(message) {
    const id = messageNextId;
    messages.value.push({
      id,
      ...message
    });
    messageNextId++;
    if (message.timeout) {
      setTimeout(() => {
        hideMessage(id);
      }, message.timeout);
    }
  }

  function hideMessage(id) {
    messages.value = messages.value.filter((m) => m.id !== id);
  }

  return {
    messages,
    showMessage,
    hideMessage
  };
}
