# DEPI Chatbot Project

<div align="center"> 
  <img src="https://m.gomhuriaonline.com/Upload/News/10-12-2023_16_05_20_GomhuriaOnline_331702217120.png" alt="Logo" width="200"> 
  <img src="https://static.vecteezy.com/system/resources/previews/026/309/247/non_2x/robot-chat-or-chat-bot-logo-modern-conversation-automatic-technology-logo-design-template-vector.jpg" alt="Logo" width="300">
</div>


Welcome to the **DEPI Chatbot Project** repository! This project is a **conversational AI chatbot** designed to assist users in answering questions, providing information, and automating tasks. The chatbot is built using **Natural Language Processing (NLP)** and **Machine Learning (ML)** techniques, making it capable of understanding and responding to user queries in a human-like manner.

---

## Table of Contents
1. [Overview](#overview)
2. [Motivation](#motivation)
3. [Features](#features)
4. [Technologies Used](#technologies-used)
5. [Dataset](#dataset)
6. [How It Works](#how-it-works)
7. [Installation](#installation)
8. [Usage](#usage)
9. [Results](#results)
10. [Future Work](#future-work)
11. [Contributing](#contributing)
12. [Acknowledgments](#acknowledgments)
13. [License](#license)

---

## Overview

The project aims to build a **RAG (Retrieval-Augmented Generation) system** to answer questions related to the **"Digital Egypt Pioneers Initiative"** using **NLP (Natural Language Processing) techniques**. First, data is collected from the initiative's website through web scraping to extract relevant textual content. Then, the model **"AbderrahmanSkiredj1/Arabic_text_embedding_for_sts"** is used to convert the extracted sentences into vector embeddings, allowing the text to be represented in a digital format for processing. These embeddings are stored in a Chroma database to facilitate easy retrieval of information later. When a user submits a question, the system searches for the most relevant embeddings in the database, which are then passed to the GPT-Turbo model to generate an appropriate answer based on the context. Finally, the project is deployed on Azure, with performance tracking and continuous improvement to ensure high-quality answers are provided, offering users the best experience as they engage with the "Digital Egypt Pioneers Initiative".

---

## Motivation
In today's digital world, businesses and organizations are increasingly relying on chatbots to improve customer engagement and streamline operations. The motivation behind this project is to:
- **Enhance User Experience**: Provide instant and accurate responses to user queries.
- **Automate Tasks**: Reduce the workload on human agents by automating repetitive tasks.
- **Improve Accessibility**: Make information and services more accessible to users through conversational interfaces.

---

## Features
- **Natural Language Understanding (NLU)**: The chatbot can understand and process user queries in natural language.
- **Context-Aware Responses**: Maintains context during conversations for more meaningful interactions.
- **Multi-Platform Support**: Can be integrated into websites, mobile apps, and messaging platforms.
- **Customizable Responses**: Allows for easy customization of responses based on specific use cases.
- **Pre-trained Models**: Utilizes state-of-the-art NLP models like **BERT**, **GPT**, and **T5** for high-quality responses.

---

## Technologies Used
- **Programming Languages**: Python
- **NLP Libraries**: NLTK, SpaCy, Hugging Face Transformers
- **Machine Learning Frameworks**: TensorFlow, PyTorch
- **Pre-trained Models**: BERT, GPT, T5
- **Web Development**: Flask (for backend), HTML5, CSS3, JavaScript
- **Database**: SQLite (for storing conversation history)

---

## Dataset
The chatbot is trained on a variety of datasets, including:
- **OpenSubtitles Dataset**: A large dataset of conversational data.
- **Cornell Movie Dialogues Corpus**: Contains dialogues from movies, useful for training conversational models.
- **Custom Datasets**: Domain-specific datasets tailored to the chatbot's use case.

The datasets are preprocessed to remove noise and ensure consistency before being used for model training.

---

## How It Works
1. **User Input**: The user types or speaks a query.
2. **Preprocessing**: The input is cleaned and tokenized to prepare it for the NLP model.
3. **Model Prediction**: The input is fed into the NLP model, which generates a response.
4. **Response Display**: The chatbot displays the generated response to the user.
5. **Context Management**: The chatbot maintains context for follow-up questions.

---

## Installation
To run this project locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/FathyHesham/DEPI_CHATBOT_PROJECT.git
   cd DEPI_CHATBOT_PROJECT
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**:
   ```bash
   python app.py
   ```

4. **Access the Web Interface**:
   Open your browser and go to `http://127.0.0.1:5000/` to interact with the chatbot.

---

## Usage
1. **Home Page**: Start by typing your query in the chatbox.
2. **Chat Interface**: The chatbot will process your query and display the response.
3. **Contextual Conversations**: Ask follow-up questions, and the chatbot will maintain context for a seamless conversation.

---

## Results
The chatbot provides accurate and context-aware responses, making it a reliable tool for user interaction. Below is an example of a conversation:

- **User**: ما هي مدة المبادرة؟
- **Chatbot**: مدة المنحة هي ستة أشهر، تشمل ٤ أشهر للمحاور الفنية والمهارات المطلوبة للعمل الحر.

- **User**: ما هو نظام المنحة؟
- **Chatbot**: نظام الدراسة بالمبادرة تدريب بنظام التدريب الهجين والذي يتمثل بنسبة ٧٥% تعليم عن بعد ٢٥% جلسات حضورية في أحد مراكز التدريب المتخصصة لذا يجب أن يتوافر لديكم جهاز كمبيوتر أو لابتوب مزودين بكاميرا ومايك وإنترنت لحضور جلسات التدريب عن بعد بأكمل وجه مع الأخذ في الاعتبار وجود بديل لانقطاع الكهرباء مثل شحن الحاسب الشخصي الخاص بالمتقدم او كارت إنترنت او تغيير المكان. يتم التدريب ثلاث مرات أسبوعيا، مرتين عن بعد ومرة في مركز التدريب بواقع ٩ ساعات أسبوعية، بالإضافة إلى ٣ ساعات للتمارين التطبيقية والمشاريع، ويجب على المتقدم الالتزام بالحضور الفعلي والالتزام بالنظام التدريبي للمبادرة للجلسات عن بعد والجلسات الحضورية. يتم التوقف عن الدراسة للطلاب خلال فترة الامتحانات النهائية لمدة شهر واحد ولا تتوقف الدراسة بالنسبة للمتقدمين من فئة الخريجين. يشترط على المتدرب الالتزام بحضور ٧٠% من الجلسات الحضورية و ٧٠% من الجلسات عن بعد وذلك فى جميع محاور الدراسة. يجب على المتدرب في المسارات الوظيفية الخاصة بالعمل الحر الحصول على عدد حد أدنى ٣ مهام من أحد منصات العمل الحر أو ما يعادل ٣٠٠ دولار كحد أدنى حتى يكون قد أتم العملية التدريبية بنجاح ويتم ذلك خلال فترة التدريب التقني أو في فترة الإرشاد المهني للعمل الحر. يتم منح المتدرب شهادة إتمام التدريب وفقا لعدد الساعات التدريبية لكل مسار تدريبي معتمدة من وزارة الاتصالات وتكنولوجيا المعلومات وذلك بعد انتهاء التدريب وإتمام المتدرب كافة متطلبات المسار التدريبي وتنفيذ المشروع المطلوب والحصول بنجاح على عدد ٣ مهام على الأقل من أحد منصات العمل الحر.


---

## Future Work
1. **Multi-Language Support**: Extend the chatbot to support multiple languages.
2. **Integration with APIs**: Allow the chatbot to fetch real-time data from external APIs.
3. **Voice Support**: Add voice input and output capabilities for a more interactive experience.
4. **Advanced Context Management**: Improve the chatbot's ability to handle complex, multi-turn conversations.

---

## Contributing
We welcome contributions to this project! If you'd like to contribute, please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes.
4. Submit a pull request.

---

## License
This project is licensed under the **MIT License**. Feel free to use, modify, and distribute the code as per the terms of the license.

```
MIT License

Copyright (c) 2023 Fathy Hesham

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## Contact
For any inquiries or further information, feel free to reach out:

- **Mail**: [fathyhesham2001@gmail.com](mailto:fathyhesham2001@gmail.com)
- **LinkedIn**: [Fathy Hesham Fathy](https://www.linkedin.com/in/fathy-hesham-fathy/)

---

**Thank you for visiting our project!** 🚀
