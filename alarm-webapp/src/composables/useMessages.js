import { ref } from "vue";

export default function useMessages() {
  let messageNextId = 0;
  const messages = ref([]);

  function showMessage(type, text, timeout) {
    const id = messageNextId;
    messages.value.push({
      id,
      type,
      text,
      timeout
    });
    messageNextId++;
    if (timeout) {
      setTimeout(() => {
        hideMessage(id);
      }, timeout);
    }
  }

  function hideMessage(id) {
    messages.value = messages.value.filter((m) => m.id !== id);
  }

  return {
    messages,
    showMessage,
    showError: (...args) => showMessage("error", ...args),
    hideMessage
  };
}
