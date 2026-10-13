(() => {
  const status = document.getElementById('copy-status');
  document.querySelectorAll('[data-copy]').forEach((button) => {
    const originalLabel = button.textContent;
    button.addEventListener('click', async () => {
      const source = document.getElementById(button.dataset.copy);
      if (!source) return;
      try {
        if (!navigator.clipboard || !window.isSecureContext) throw new Error('Clipboard unavailable');
        await navigator.clipboard.writeText(source.textContent.trim());
        status.textContent = `${originalLabel.replace(/^Copy /, '')} copied. Paste it into your AI chat when ready.`;
      } catch (_) {
        const range = document.createRange();
        range.selectNodeContents(source);
        const selection = window.getSelection();
        selection.removeAllRanges();
        selection.addRange(range);
        status.textContent = 'Automatic copy is unavailable. The prompt is selected; use your usual copy command, or select and copy it manually.';
      }
      button.textContent = status.textContent.startsWith('Automatic') ? 'Select and copy manually' : 'Copied';
      window.setTimeout(() => { button.textContent = originalLabel; }, 2500);
    });
  });
  const revealTarget = () => {
    const id = window.location.hash.slice(1);
    if (!id) return;
    const target = document.getElementById(id);
    if (target && target.tagName === 'DETAILS') target.open = true;
  };
  window.addEventListener('hashchange', revealTarget);
  revealTarget();
})();