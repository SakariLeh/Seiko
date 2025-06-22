    const socket = io();


    socket.on('connect', () => {
      socket.emit('join', { chat_id: chatId });
    });

    socket.on('message', (data) => {
        const wrapper = document.createElement('div');
        wrapper.classList.add('message-wrapper');
        wrapper.classList.add(data.sender_id === currentUserId ? 'my-wrapper' : 'other-wrapper');

        const senderEl = document.createElement('div');
        senderEl.classList.add('sender-name');
        senderEl.textContent = data.sender_id === currentUserId ? 'Вы' : data.sender_name;

        const messageEl = document.createElement('div');
        messageEl.classList.add('message');
        messageEl.classList.add(data.sender_id === currentUserId ? 'my-message' : 'other-message');
        messageEl.textContent = data.text;

        wrapper.appendChild(senderEl);
        wrapper.appendChild(messageEl);
        document.getElementById('messages').appendChild(wrapper);
        scrollToBottom();
    });

    function send() {
        const input = document.getElementById('myMessage');
        const text = input.value.trim();
        if (text === '') return;
        socket.emit('chat_message', {
            chat_id: chatId,
            text: text,
            sender_id: currentUserId 
        });


        input.value = '';
    }

    function scrollToBottom() {
      const container = document.getElementById('messages');
      container.scrollTop = container.scrollHeight;
    }

    scrollToBottom();



    document.getElementById("myMessage").addEventListener("keydown", function (e) {
        if (e.key === "Enter") send();
    });

    document.getElementById("myMessage").focus();




    socket.on('message_deleted', (data) => {
      const msgEl = document.querySelector(`[data-message-id="${data.message_id}"]`);
      if (msgEl) {
        msgEl.innerText = '[сообщение удалено]';
        msgEl.style.fontStyle = 'italic';
        msgEl.style.color = '#888';
      }
    });


    document.getElementById('messages').addEventListener('contextmenu', function (e) {
      e.preventDefault();
      const messageEl = e.target.closest('.message');
      if (!messageEl) return;

      const messageId = messageEl.dataset.messageId;
      if (!messageId) return;

      const confirmDelete = confirm('Удалить сообщение?');
      if (!confirmDelete) return;

      socket.emit('delete_message', {
        message_id: parseInt(messageId),
        chat_id: chatId,
        user_id: currentUserId
      });
    });



    function deleteMessage(messageId) {
      if (confirm('Удалить сообщение?')) {
        socket.emit('delete_message', {
          message_id: messageId,
          chat_id: chatId,
          user_id: currentUserId
        });
      }
    }


    function copyMessage(btn) {
      const msgText = btn.parentElement.querySelector('.message-text').innerText;
      navigator.clipboard.writeText(msgText).then(() => {
        btn.innerText = '✔️';
        setTimeout(() => {
          btn.innerText = '📋';
        }, 1000);
      });
    }