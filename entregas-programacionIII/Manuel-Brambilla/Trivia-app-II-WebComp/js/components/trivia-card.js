class TriviaCard extends HTMLElement {
    constructor() {
        super();
        this._shadow = this.attachShadow({ mode: 'open' }); // Crear un shadow DOM para encapsular estilos y estructura
        this._pregunta = null; // Inicializar la propiedad pregunta
    }

    // setter para la propiedad pregunta, que se usará para actualizar el contenido del componente
    set pregunta(valor) {
        this._pregunta = valor;
        this._render(); // Renderizar el componente cada vez que se actualice la pregunta 
    }

    _render() {
        if (!this._pregunta) return;

        const opciones = mezclar([this._pregunta.correct_answer,
             ...this._pregunta.incorrect_answers
        ]);
        this._shadow.innerHTML = `
            <style>
                :host {
                    display: block;
                    padding: 1em;
                }
                .pregunta {
                    font-size: 1.2em;
                    margin-bottom: 1em;
                }
                .opciones {
                    display: flex;
                    flex-direction: column;
                    gap: 0.3em;
                }
                button {
                    padding: 0.5em 1em;
                    font-size: 1em;
                    border: 1px solid #ccc;
                    border-radius: 6px;
                    cursor: pointer;
                    background-color: #f9f9f9;
                }
                button:hover {
                    background-color: #f0f0f0;
                }
                button.correct {
                    background-color: #4caf50;
                    color: white;
                }
                button.incorrect {
                    background-color: #f44336;
                    color: white;
                }
                button:disabled {
                    cursor: not-allowed;
                    opacity: 0.6;
                }
                button.correct, button.incorrect {
                    opacity: 1;
                }
            </style>

            <p class="pregunta">${decodificarHTML(this._pregunta.question)}</p>
            <div class="opciones">
                ${opciones.map((op) => `
                    <button data-respuesta="${op}">${decodificarHTML(op)}</button>
                `).join('')}
            </div>
        `;

        this._agregarEventos();
    }

    _agregarEventos() {
        const botones = this._shadow.querySelectorAll('button');

        botones.forEach((btn) => {
            btn.addEventListener('click', () => {
                this._manejarRespuesta(btn);
            });
        });
    }

    _manejarRespuesta(btn) {
        this._deshabilitarBotones();
        const opcionElegida = btn.dataset.respuesta;
        const esCorrecta = opcionElegida === this._pregunta.correct_answer;

        this._mostrarFeedback(btn, esCorrecta);

        setTimeout(() => {
            this._emitirRespuesta(esCorrecta);
        }, 1000);
    }

    _deshabilitarBotones() {
        this._shadow.querySelectorAll('button').forEach(b => b.disabled = true);
    }

    _mostrarFeedback(btn, esCorrecta) {
        btn.classList.add(esCorrecta ? 'correct' : 'incorrect');
        if (!esCorrecta) {
            this._shadow.querySelectorAll('button').forEach(btn => {
                if (btn.dataset.respuesta === this._pregunta.correct_answer) {
                    btn.classList.add('correct');
                }
            });  
        }
    }

    _emitirRespuesta(esCorrecta) {
        this.dispatchEvent(new CustomEvent('respondida', {
            detail: { correcta: esCorrecta },
            bubbles: true,
        }));
    }
}

customElements.define('trivia-card', TriviaCard);