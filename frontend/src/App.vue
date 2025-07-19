<template>
  <div id="app" :class="[
    'min-h-screen transition-all duration-500',
    isDark
      ? 'bg-gradient-to-br from-gray-900 via-slate-800 to-gray-900'
      : 'bg-gradient-to-br from-sky-50 via-pink-50 to-white'
  ]">
    <!-- Header -->
    <header :class="[
      'backdrop-blur-sm shadow-lg border-b transition-all duration-500',
      isDark
        ? 'bg-gray-800/80 border-gray-700'
        : 'bg-white/80 border-pink-100'
    ]">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex justify-between items-center py-6">
          <div class="flex items-center">
            <div class="flex-shrink-0">
              <img src="./assets/logo.png" alt="AutoResum Logo" class="h-12 w-auto mr-3">
            </div>
            <div>
              <h1 :class="[
                'text-3xl font-bold bg-clip-text text-transparent transition-all duration-500',
                isDark
                  ? 'bg-gradient-to-r from-sky-400 to-pink-400'
                  : 'bg-gradient-to-r from-sky-600 to-pink-600'
              ]">
                AutoResum
              </h1>
              <p :class="[
                'text-sm transition-colors duration-500',
                isDark ? 'text-gray-300' : 'text-gray-600'
              ]">Résumé automatique de texte avec IA</p>
            </div>
          </div>
          <div class="flex items-center space-x-4">
            <button @click="toggleTheme" :class="[
              'p-3 rounded-xl transition-all duration-300 shadow-md hover:shadow-lg',
              isDark
                ? 'bg-gradient-to-r from-gray-700 to-gray-600 hover:from-gray-600 hover:to-gray-500'
                : 'bg-gradient-to-r from-sky-100 to-pink-100 hover:from-sky-200 hover:to-pink-200'
            ]">
              <svg v-if="isDark" class="w-5 h-5 text-yellow-400" fill="currentColor" viewBox="0 0 20 20">
                <path fill-rule="evenodd"
                  d="M10 2a1 1 0 011 1v1a1 1 0 11-2 0V3a1 1 0 011-1zm4 8a4 4 0 11-8 0 4 4 0 018 0zm-.464 4.95l.707.707a1 1 0 001.414-1.414l-.707-.707a1 1 0 00-1.414 1.414zm2.12-10.607a1 1 0 010 1.414l-.706.707a1 1 0 11-1.414-1.414l.707-.707a1 1 0 011.414 0zM17 11a1 1 0 100-2h-1a1 1 0 100 2h1zm-7 4a1 1 0 011 1v1a1 1 0 11-2 0v-1a1 1 0 011-1zM5.05 6.464A1 1 0 106.465 5.05l-.708-.707a1 1 0 00-1.414 1.414l.707.707zm1.414 8.486l-.707.707a1 1 0 01-1.414-1.414l.707-.707a1 1 0 011.414 1.414zM4 11a1 1 0 100-2H3a1 1 0 000 2h1z"
                  clip-rule="evenodd"></path>
              </svg>
              <svg v-else class="w-5 h-5 text-sky-600" fill="currentColor" viewBox="0 0 20 20">
                <path d="M17.293 13.293A8 8 0 016.707 2.707a8.001 8.001 0 1010.586 10.586z"></path>
              </svg>
            </button>
          </div>
        </div>
      </div>
    </header>

    <!-- Main Content -->
    <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
        <!-- Input Section -->
        <div class="space-y-6">
          <div :class="[
            'backdrop-blur-sm rounded-2xl shadow-xl border p-8 transition-all duration-500',
            isDark
              ? 'bg-gray-800/80 border-gray-700'
              : 'bg-white/80 border-pink-100'
          ]">
            <h2 :class="[
              'text-2xl font-bold mb-6 flex items-center transition-colors duration-500',
              isDark ? 'text-gray-100' : 'text-gray-900'
            ]">
              <div :class="[
                'w-8 h-8 rounded-lg flex items-center justify-center mr-3',
                isDark
                  ? 'bg-gradient-to-r from-sky-400 to-pink-400'
                  : 'bg-gradient-to-r from-sky-500 to-pink-500'
              ]">
                <svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                    d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z">
                  </path>
                </svg>
              </div>
              Texte à résumer
            </h2>

            <!-- Language Selection -->
            <div class="mb-6">
              <label :class="[
                'block text-sm font-semibold mb-3 transition-colors duration-500',
                isDark ? 'text-gray-300' : 'text-gray-700'
              ]">Langue</label>
              <select v-model="selectedLanguage" :class="[
                'w-full px-4 py-3 border rounded-xl focus:outline-none focus:ring-2 focus:border-transparent transition-all duration-300',
                isDark
                  ? 'border-gray-600 focus:ring-sky-400 bg-gray-700/50 text-gray-100'
                  : 'border-pink-200 focus:ring-sky-500 bg-white/50 text-gray-900'
              ]">
                <option value="fr">Français</option>
                <option value="en">Anglais</option>
                <option value="auto">Détection automatique</option>
              </select>
            </div>

            <!-- Text Input -->
            <div class="mb-6">
              <label :class="[
                'block text-sm font-semibold mb-3 transition-colors duration-500',
                isDark ? 'text-gray-300' : 'text-gray-700'
              ]">
                Texte (minimum 50 caractères)
              </label>
              <textarea v-model="inputText" @input="updateTextStats" placeholder="Collez votre texte ici..." :class="[
                'w-full h-64 px-4 py-3 border rounded-xl focus:outline-none focus:ring-2 focus:border-transparent resize-none transition-all duration-300',
                isDark
                  ? 'border-gray-600 focus:ring-sky-400 bg-gray-700/50 text-gray-100 placeholder-gray-400'
                  : 'border-pink-200 focus:ring-sky-500 bg-white/50 text-gray-900 placeholder-gray-500',
                inputText.length > 0 && inputText.length < 50 ? 'border-red-400 ring-red-300' : ''
              ]"></textarea>
              <div class="flex justify-between items-center mt-3">
                <span :class="[
                  'text-sm transition-colors duration-500',
                  isDark ? 'text-gray-400' : 'text-gray-500'
                ]">
                  {{ inputText.length }} caractères
                </span>
                <span v-if="inputText.length > 0 && inputText.length < 50" class="text-sm text-red-400 font-medium">
                  Minimum 50 caractères requis
                </span>
              </div>
            </div>

            <!-- Summary Options -->
            <div class="grid grid-cols-2 gap-4 mb-8">
              <div>
                <label :class="[
                  'block text-sm font-semibold mb-3 transition-colors duration-500',
                  isDark ? 'text-gray-300' : 'text-gray-700'
                ]">Longueur max</label>
                <input v-model.number="maxLength" type="number" min="50" max="500" :class="[
                  'w-full px-4 py-3 border rounded-xl focus:outline-none focus:ring-2 focus:border-transparent transition-all duration-300',
                  isDark
                    ? 'border-gray-600 focus:ring-sky-400 bg-gray-700/50 text-gray-100'
                    : 'border-pink-200 focus:ring-sky-500 bg-white/50 text-gray-900'
                ]">
              </div>
              <div>
                <label :class="[
                  'block text-sm font-semibold mb-3 transition-colors duration-500',
                  isDark ? 'text-gray-300' : 'text-gray-700'
                ]">Longueur min</label>
                <input v-model.number="minLength" type="number" min="20" max="200" :class="[
                  'w-full px-4 py-3 border rounded-xl focus:outline-none focus:ring-2 focus:border-transparent transition-all duration-300',
                  isDark
                    ? 'border-gray-600 focus:ring-sky-400 bg-gray-700/50 text-gray-100'
                    : 'border-pink-200 focus:ring-sky-500 bg-white/50 text-gray-900'
                ]">
              </div>
            </div>

            <!-- Action Buttons -->
            <div class="flex space-x-4">
              <button @click="generateSummary" :disabled="!canGenerateSummary || isLoading" :class="[
                'flex-1 text-white px-6 py-3 rounded-xl focus:outline-none disabled:opacity-50 disabled:cursor-not-allowed transition-all duration-300 shadow-lg hover:shadow-xl transform hover:-translate-y-1',
                isDark
                  ? 'bg-gradient-to-r from-sky-500 to-pink-500 hover:from-sky-600 hover:to-pink-600 focus:ring-sky-400'
                  : 'bg-gradient-to-r from-sky-500 to-pink-500 hover:from-sky-600 hover:to-pink-600 focus:ring-sky-500'
              ]">
                <svg v-if="isLoading" class="animate-spin -ml-1 mr-3 h-5 w-5 text-white"
                  xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                  <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                  <path class="opacity-75" fill="currentColor"
                    d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z">
                  </path>
                </svg>
                {{ isLoading ? 'Génération...' : 'Générer le résumé' }}
              </button>
              <button @click="analyzeText" :disabled="!canGenerateSummary || isLoading" :class="[
                'px-6 py-3 border-2 rounded-xl focus:outline-none disabled:opacity-50 disabled:cursor-not-allowed transition-all duration-300',
                isDark
                  ? 'border-gray-600 text-gray-300 hover:bg-gray-700 focus:ring-sky-400 bg-gray-800/50'
                  : 'border-pink-200 text-gray-700 hover:bg-pink-50 focus:ring-sky-500 bg-white/50'
              ]">
                Analyser
              </button>
            </div>
          </div>

          <!-- Text Statistics -->
          <div v-if="textStats" :class="[
            'backdrop-blur-sm rounded-2xl shadow-xl border p-8 transition-all duration-500',
            isDark
              ? 'bg-gray-800/80 border-gray-700'
              : 'bg-white/80 border-pink-100'
          ]">
            <h3 :class="[
              'text-xl font-bold mb-6 flex items-center transition-colors duration-500',
              isDark ? 'text-gray-100' : 'text-gray-900'
            ]">
              <div :class="[
                'w-8 h-8 rounded-lg flex items-center justify-center mr-3',
                isDark
                  ? 'bg-gradient-to-r from-pink-400 to-sky-400'
                  : 'bg-gradient-to-r from-pink-500 to-sky-500'
              ]">
                <svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                    d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z">
                  </path>
                </svg>
              </div>
              Statistiques du texte
            </h3>
            <div class="grid grid-cols-2 gap-6">
              <div :class="[
                'text-center p-4 rounded-xl',
                isDark
                  ? 'bg-gradient-to-br from-gray-700 to-gray-600'
                  : 'bg-gradient-to-br from-sky-50 to-pink-50'
              ]">
                <div :class="[
                  'text-3xl font-bold bg-clip-text text-transparent',
                  isDark
                    ? 'bg-gradient-to-r from-sky-400 to-pink-400'
                    : 'bg-gradient-to-r from-sky-600 to-pink-600'
                ]">{{ textStats.word_count }}</div>
                <div :class="[
                  'text-sm font-medium transition-colors duration-500',
                  isDark ? 'text-gray-300' : 'text-gray-600'
                ]">Mots</div>
              </div>
              <div :class="[
                'text-center p-4 rounded-xl',
                isDark
                  ? 'bg-gradient-to-br from-gray-600 to-gray-700'
                  : 'bg-gradient-to-br from-pink-50 to-sky-50'
              ]">
                <div :class="[
                  'text-3xl font-bold bg-clip-text text-transparent',
                  isDark
                    ? 'bg-gradient-to-r from-pink-400 to-sky-400'
                    : 'bg-gradient-to-r from-pink-600 to-sky-600'
                ]">{{ textStats.sentence_count }}</div>
                <div :class="[
                  'text-sm font-medium transition-colors duration-500',
                  isDark ? 'text-gray-300' : 'text-gray-600'
                ]">Phrases</div>
              </div>
              <div :class="[
                'text-center p-4 rounded-xl',
                isDark
                  ? 'bg-gradient-to-br from-gray-700 to-gray-600'
                  : 'bg-gradient-to-br from-sky-50 to-pink-50'
              ]">
                <div :class="[
                  'text-3xl font-bold bg-clip-text text-transparent',
                  isDark
                    ? 'bg-gradient-to-r from-sky-400 to-pink-400'
                    : 'bg-gradient-to-r from-sky-600 to-pink-600'
                ]">{{ textStats.reading_time }}</div>
                <div :class="[
                  'text-sm font-medium transition-colors duration-500',
                  isDark ? 'text-gray-300' : 'text-gray-600'
                ]">Min de lecture</div>
              </div>
              <div :class="[
                'text-center p-4 rounded-xl',
                isDark
                  ? 'bg-gradient-to-br from-gray-600 to-gray-700'
                  : 'bg-gradient-to-br from-pink-50 to-sky-50'
              ]">
                <div :class="[
                  'text-3xl font-bold bg-clip-text text-transparent',
                  isDark
                    ? 'bg-gradient-to-r from-pink-400 to-sky-400'
                    : 'bg-gradient-to-r from-pink-600 to-sky-600'
                ]">{{ textStats.avg_sentence_length }}</div>
                <div :class="[
                  'text-sm font-medium transition-colors duration-500',
                  isDark ? 'text-gray-300' : 'text-gray-600'
                ]">Mots/phrase</div>
              </div>
            </div>
          </div>
        </div>

        <!-- Output Section -->
        <div class="space-y-6">
          <!-- Summary Result -->
          <div v-if="summaryResult" :class="[
            'backdrop-blur-sm rounded-2xl shadow-xl border p-8 transition-all duration-500',
            isDark
              ? 'bg-gray-800/80 border-gray-700'
              : 'bg-white/80 border-pink-100'
          ]">
            <div class="flex justify-between items-center mb-6">
              <h2 :class="[
                'text-2xl font-bold flex items-center transition-colors duration-500',
                isDark ? 'text-gray-100' : 'text-gray-900'
              ]">
                <div :class="[
                  'w-8 h-8 rounded-lg flex items-center justify-center mr-3',
                  isDark
                    ? 'bg-gradient-to-r from-green-400 to-sky-400'
                    : 'bg-gradient-to-r from-green-500 to-sky-500'
                ]">
                  <svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                      d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                  </svg>
                </div>
                Résumé généré
              </h2>
              <button @click="copyToClipboard(summaryResult.summary)" :class="[
                'p-3 rounded-xl transition-all duration-300 shadow-md hover:shadow-lg',
                isDark
                  ? 'bg-gradient-to-r from-gray-700 to-gray-600 hover:from-gray-600 hover:to-gray-500'
                  : 'bg-gradient-to-r from-sky-100 to-pink-100 hover:from-sky-200 hover:to-pink-200'
              ]">
                <svg :class="[
                  'w-5 h-5 transition-colors duration-500',
                  isDark ? 'text-sky-400' : 'text-sky-600'
                ]" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                    d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z">
                  </path>
                </svg>
              </button>
            </div>

            <div :class="[
              'rounded-xl p-6 mb-6 border',
              isDark
                ? 'bg-gradient-to-br from-gray-700 to-gray-600 border-gray-600'
                : 'bg-gradient-to-br from-sky-50 to-pink-50 border-sky-100'
            ]">
              <p :class="[
                'leading-relaxed text-lg transition-colors duration-500',
                isDark ? 'text-gray-200' : 'text-gray-800'
              ]">{{ summaryResult.summary }}</p>
            </div>

            <!-- Summary Metrics -->
            <div class="grid grid-cols-2 gap-4 mb-6">
              <div :class="[
                'text-center p-4 rounded-xl border',
                isDark
                  ? 'bg-gradient-to-br from-gray-700 to-gray-600 border-gray-600'
                  : 'bg-gradient-to-br from-green-50 to-sky-50 border-green-100'
              ]">
                <div class="text-2xl font-bold text-green-500">{{ summaryResult.compression_ratio }}%</div>
                <div :class="[
                  'text-sm font-medium transition-colors duration-500',
                  isDark ? 'text-gray-300' : 'text-gray-600'
                ]">Compression</div>
              </div>
              <div :class="[
                'text-center p-4 rounded-xl border',
                isDark
                  ? 'bg-gradient-to-br from-gray-600 to-gray-700 border-gray-600'
                  : 'bg-gradient-to-br from-sky-50 to-pink-50 border-sky-100'
              ]">
                <div class="text-2xl font-bold text-sky-500">{{ summaryResult.reading_time }}</div>
                <div :class="[
                  'text-sm font-medium transition-colors duration-500',
                  isDark ? 'text-gray-300' : 'text-gray-600'
                ]">Min de lecture</div>
              </div>
            </div>

            <!-- Keywords -->
            <div v-if="summaryResult.keywords.length > 0">
              <h4 :class="[
                'text-sm font-semibold mb-3 transition-colors duration-500',
                isDark ? 'text-gray-300' : 'text-gray-700'
              ]">Mots-clés</h4>
              <div class="flex flex-wrap gap-2">
                <span v-for="keyword in summaryResult.keywords" :key="keyword" :class="[
                  'px-3 py-2 text-sm rounded-full font-medium border transition-all duration-300',
                  isDark
                    ? 'bg-gradient-to-r from-gray-700 to-gray-600 text-sky-300 border-gray-600'
                    : 'bg-gradient-to-r from-sky-100 to-pink-100 text-sky-800 border-sky-200'
                ]">
                  {{ keyword }}
                </span>
              </div>
            </div>
          </div>

          <!-- Analysis Result -->
          <div v-if="analysisResult" :class="[
            'backdrop-blur-sm rounded-2xl shadow-xl border p-8 transition-all duration-500',
            isDark
              ? 'bg-gray-800/80 border-gray-700'
              : 'bg-white/80 border-pink-100'
          ]">
            <h3 :class="[
              'text-xl font-bold mb-6 flex items-center transition-colors duration-500',
              isDark ? 'text-gray-100' : 'text-gray-900'
            ]">
              <div :class="[
                'w-8 h-8 rounded-lg flex items-center justify-center mr-3',
                isDark
                  ? 'bg-gradient-to-r from-purple-400 to-pink-400'
                  : 'bg-gradient-to-r from-purple-500 to-pink-500'
              ]">
                <svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                    d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z">
                  </path>
                </svg>
              </div>
              Analyse du texte
            </h3>

            <!-- Sentiment Analysis -->
            <div class="mb-6">
              <h4 :class="[
                'text-sm font-semibold mb-3 transition-colors duration-500',
                isDark ? 'text-gray-300' : 'text-gray-700'
              ]">Sentiment</h4>
              <div class="grid grid-cols-2 gap-4">
                <div :class="[
                  'text-center p-4 rounded-xl border',
                  isDark
                    ? 'bg-gradient-to-br from-gray-700 to-gray-600 border-gray-600'
                    : 'bg-gradient-to-br from-green-50 to-sky-50 border-green-100'
                ]">
                  <div class="text-lg font-bold" :class="getSentimentColor(analysisResult.sentiment.compound)">
                    {{ getSentimentLabel(analysisResult.sentiment.compound) }}
                  </div>
                  <div :class="[
                    'text-sm font-medium transition-colors duration-500',
                    isDark ? 'text-gray-300' : 'text-gray-600'
                  ]">Global</div>
                </div>
                <div :class="[
                  'text-center p-4 rounded-xl border',
                  isDark
                    ? 'bg-gradient-to-br from-gray-600 to-gray-700 border-gray-600'
                    : 'bg-gradient-to-br from-sky-50 to-pink-50 border-sky-100'
                ]">
                  <div class="text-lg font-bold text-green-500">{{ (analysisResult.sentiment.positive * 100).toFixed(1)
                    }}%</div>
                  <div :class="[
                    'text-sm font-medium transition-colors duration-500',
                    isDark ? 'text-gray-300' : 'text-gray-600'
                  ]">Positif</div>
                </div>
                <div :class="[
                  'text-center p-4 rounded-xl border',
                  isDark
                    ? 'bg-gradient-to-br from-gray-700 to-gray-600 border-gray-600'
                    : 'bg-gradient-to-br from-red-50 to-pink-50 border-red-100'
                ]">
                  <div class="text-lg font-bold text-red-400">{{ (analysisResult.sentiment.negative * 100).toFixed(1)
                    }}%</div>
                  <div :class="[
                    'text-sm font-medium transition-colors duration-500',
                    isDark ? 'text-gray-300' : 'text-gray-600'
                  ]">Négatif</div>
                </div>
                <div :class="[
                  'text-center p-4 rounded-xl border',
                  isDark
                    ? 'bg-gradient-to-br from-gray-600 to-gray-700 border-gray-600'
                    : 'bg-gradient-to-br from-gray-50 to-sky-50 border-gray-100'
                ]">
                  <div class="text-lg font-bold text-gray-400">{{ (analysisResult.sentiment.neutral * 100).toFixed(1)
                    }}%</div>
                  <div :class="[
                    'text-sm font-medium transition-colors duration-500',
                    isDark ? 'text-gray-300' : 'text-gray-600'
                  ]">Neutre</div>
                </div>
              </div>
            </div>

            <!-- Entities -->
            <div v-if="analysisResult.entities.length > 0" class="mb-4">
              <h4 :class="[
                'text-sm font-semibold mb-3 transition-colors duration-500',
                isDark ? 'text-gray-300' : 'text-gray-700'
              ]">Entités nommées</h4>
              <div class="flex flex-wrap gap-2">
                <span v-for="entity in analysisResult.entities" :key="entity.text" :class="[
                  'px-3 py-2 text-sm rounded-full font-medium border transition-all duration-300',
                  isDark
                    ? 'bg-gradient-to-r from-gray-700 to-gray-600 text-sky-300 border-gray-600'
                    : 'bg-gradient-to-r from-sky-100 to-pink-100 text-sky-800 border-sky-200'
                ]" :title="entity.description">
                  {{ entity.text }} ({{ entity.label }})
                </span>
              </div>
            </div>
          </div>

          <!-- Error Message -->
          <div v-if="errorMessage" :class="[
            'border rounded-2xl p-6 transition-all duration-500',
            isDark
              ? 'bg-gradient-to-r from-red-900/50 to-pink-900/50 border-red-700'
              : 'bg-gradient-to-r from-red-50 to-pink-50 border-red-200'
          ]">
            <div class="flex">
              <div class="w-8 h-8 bg-red-500 rounded-lg flex items-center justify-center mr-4">
                <svg class="w-5 h-5 text-white" fill="currentColor" viewBox="0 0 20 20">
                  <path fill-rule="evenodd"
                    d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z"
                    clip-rule="evenodd"></path>
                </svg>
              </div>
              <div>
                <h3 :class="[
                  'text-lg font-semibold transition-colors duration-500',
                  isDark ? 'text-red-300' : 'text-red-800'
                ]">Erreur</h3>
                <div :class="[
                  'mt-2 transition-colors duration-500',
                  isDark ? 'text-red-200' : 'text-red-700'
                ]">{{ errorMessage }}</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script>
export default {
  name: 'App',
  data() {
    return {
      inputText: '',
      selectedLanguage: 'fr',
      maxLength: 150,
      minLength: 50,
      isLoading: false,
      summaryResult: null,
      analysisResult: null,
      textStats: null,
      errorMessage: '',
      isDark: false,
      apiBaseUrl: 'http://localhost:8000'
    }
  },
  computed: {
    canGenerateSummary() {
      return this.inputText.length >= 50 && !this.isLoading
    }
  },
  mounted() {
    // Récupérer le thème sauvegardé ou utiliser la préférence système
    const savedTheme = localStorage.getItem('theme')
    if (savedTheme) {
      this.isDark = savedTheme === 'dark'
    } else {
      // Détecter la préférence système
      this.isDark = window.matchMedia('(prefers-color-scheme: dark)').matches
    }
    this.applyTheme()
  },
  methods: {
    async generateSummary() {
      if (!this.canGenerateSummary) return

      this.isLoading = true
      this.errorMessage = ''
      this.summaryResult = null

      try {
        const response = await fetch(`${this.apiBaseUrl}/summarize`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            text: this.inputText,
            max_length: this.maxLength,
            min_length: this.minLength,
            language: this.selectedLanguage
          })
        })

        if (!response.ok) {
          const error = await response.json()
          throw new Error(error.detail || 'Erreur lors de la génération du résumé')
        }

        this.summaryResult = await response.json()

      } catch (error) {
        this.errorMessage = error.message
        console.error('Erreur:', error)
      } finally {
        this.isLoading = false
      }
    },

    async analyzeText() {
      if (!this.canGenerateSummary) return

      this.isLoading = true
      this.errorMessage = ''
      this.analysisResult = null

      try {
        const response = await fetch(`${this.apiBaseUrl}/analyze`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            text: this.inputText,
            language: this.selectedLanguage
          })
        })

        if (!response.ok) {
          const error = await response.json()
          throw new Error(error.detail || 'Erreur lors de l\'analyse')
        }

        this.analysisResult = await response.json()

      } catch (error) {
        this.errorMessage = error.message
        console.error('Erreur:', error)
      } finally {
        this.isLoading = false
      }
    },

    updateTextStats() {
      if (this.inputText.length >= 50) {
        this.textStats = {
          word_count: this.inputText.split(/\s+/).filter(word => word.length > 0).length,
          sentence_count: this.inputText.split(/[.!?]+/).filter(sentence => sentence.trim().length > 0).length,
          reading_time: Math.round(this.inputText.split(/\s+/).length / 200 * 10) / 10,
          avg_sentence_length: Math.round(this.inputText.split(/\s+/).length / Math.max(1, this.inputText.split(/[.!?]+/).filter(sentence => sentence.trim().length > 0).length))
        }
      } else {
        this.textStats = null
      }
    },

    async copyToClipboard(text) {
      try {
        await navigator.clipboard.writeText(text)
        // Optionnel: afficher une notification de succès
      } catch (err) {
        console.error('Erreur lors de la copie:', err)
      }
    },

    getSentimentLabel(compound) {
      if (compound >= 0.05) return 'Positif'
      if (compound <= -0.05) return 'Négatif'
      return 'Neutre'
    },

    getSentimentColor(compound) {
      if (compound >= 0.05) return 'text-green-500'
      if (compound <= -0.05) return 'text-red-400'
      return 'text-gray-400'
    },

    toggleTheme() {
      console.log('Toggle theme clicked, current isDark:', this.isDark)
      this.isDark = !this.isDark
      console.log('New isDark value:', this.isDark)
      this.applyTheme()
    },

    applyTheme() {
      console.log('Applying theme, isDark:', this.isDark)
      // Sauvegarder le thème dans localStorage
      localStorage.setItem('theme', this.isDark ? 'dark' : 'light')
      console.log('Theme saved to localStorage:', this.isDark ? 'dark' : 'light')

      // Appliquer le thème au document
      if (this.isDark) {
        document.documentElement.classList.add('dark')
        console.log('Dark class added to document')
      } else {
        document.documentElement.classList.remove('dark')
        console.log('Dark class removed from document')
      }

      // Forcer la mise à jour du DOM
      this.$nextTick(() => {
        console.log('DOM updated, current classes on document:', document.documentElement.className)
      })
    }
  }
}
</script>

<style>
#app {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
}

/* Animations personnalisées */
@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }

  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.bg-white\/80,
.bg-gray-800\/80 {
  animation: fadeInUp 0.6s ease-out;
}

/* Effet de glassmorphism amélioré */
.backdrop-blur-sm {
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
}

/* Hover effects pour les boutons */
button:hover {
  transform: translateY(-2px);
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

/* Gradient animé pour le titre */
@keyframes gradientShift {
  0% {
    background-position: 0% 50%;
  }

  50% {
    background-position: 100% 50%;
  }

  100% {
    background-position: 0% 50%;
  }
}

.bg-gradient-to-r.from-sky-600.to-pink-600,
.bg-gradient-to-r.from-sky-400.to-pink-400 {
  background-size: 200% 200%;
  animation: gradientShift 3s ease infinite;
}

/* Transitions fluides pour le mode sombre */
* {
  transition: background-color 0.3s ease, border-color 0.3s ease, color 0.3s ease;
}

/* Scrollbar personnalisée pour le mode sombre */
.dark ::-webkit-scrollbar {
  width: 8px;
}

.dark ::-webkit-scrollbar-track {
  background: rgba(31, 41, 55, 0.5);
}

.dark ::-webkit-scrollbar-thumb {
  background: linear-gradient(135deg, #0ea5e9 0%, #ec4899 100%);
  border-radius: 4px;
}

.dark ::-webkit-scrollbar-thumb:hover {
  background: linear-gradient(135deg, #0284c7 0%, #db2777 100%);
}
</style>
