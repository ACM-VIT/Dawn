# Various Domains of AI
"Artificial Intelligence" is a concept too broad to be studied as a single thing. Trying to engineer a single, way too complex element to behave intelligently would require the making of something like a brain. However, we are far from understanding the exact functioning of the brain to an extent we don't even know, so reverse-engineering the brain isn't quite feasible at the moment. Instead, what we do is focus on certain, <b>specific</b> aspects of exhibition of intelligence and try to find patterns <b>specific</b> to that aspect to make a program do a <b>specific</b> task. In this document, you can find a brief introduction of all the different domains that AI R&D is commonly divided into.  

<h3>Contents</h3>
<ol>
  <li> <a href="#machine-learning">Machine Learning</a></li>
  <li> <a href="#deep-learning">Deep Learning</a></li>
  <li> <a href="#reinforcement-learning">Reinforcement Learning</a></li>
  <li> <a href="#artificial-neural-networks">Artificial Neural Networks</a></li>
  <li> <a href="#image-processing">Image Processing</a></li>
  <li> <a href="#natural-language-processing">Natural Language processing</a></li>
  <li> <a href="#audio-processing">Audio processing</a></li>
</ol>
<br/>

# Machine Learning
The term itself is quite self-explanatory. Machine learning is an approch where a machine is made to <b>learn</b>. Now, the question is, what does the machine learn, and how? Well, the idea is pretty simple. As previously mentioned, finding <b>patterns</b> is important. In this case, the program is fed with a lot of <b>data</b>. By some predefined <b>mathematical</b> and <b>statistical</b> methods, the program discovers the hidden patterns and develops a generalized algorithm for that kind of data. When the machine is asked to <b>predict</b> future outcomes relating to that <b>dataset</b>, it simply puts the necessary parameters into the equation and finds the output.<br/>  

So, basically, the machine learns from historical data and becomes capable of predicting future values.<br/>
Common examples of application of machine learning are:
<ul>
  <li> Predicting stock prices based on past market conditions</li>
  <li> Predicting house prices based on previous data</li>
  <li> Predicting future behaviour of a user based on their past activity (Google does this all the time!)</li>
  <li> Weather forecasting</li>
</ul>
Here is an example of a basic <b>Car dataset</b><sup><i>(<a href="https://www.heatonresearch.com/">source</a>)</i></sup>:<br/>  
  
<img src="https://i.imgur.com/xU13umY.png"/>  
  
<b>Notice</b> how the columns are <b>labelled</b>. This type of dataset is called <b>labelled dataset</b>. <b>Machine Learning</b>, therefore, is also called <b>supervised learning</b> as it uses a labelled dataset.<br/><br/>

It should be noted that another way of fetching results through machine learning is <b>classification</b>, besides prediction. While prediction algorithms predict a discrete value, classification techniques help describe the input by choosing which class it is best suited to.<br/><br/>

For example, imagine you had to determine whether a fruit is rotten or fresh. Here, <b>rotten</b> and <b>fresh</b> are the classes. By analysing the paramters such as appearance, odour, texture, etc., you put it in the class with the most number of properties matching with that of the fruit.
<br/><br/>  

Beginners can start this [COURSE](https://in.udacity.com/course/intro-to-machine-learning--ud120-india) offered by Udacity for free

# Deep Learning
Deep learning, like Machine Learning, is also a method where the program is made to learn from historical data. The difference is that instead of creating an equation based on patterns in datasets, deep learning algorithms structure data in the form of a connected graph. The connected graph actually tends to lead to the formation of a diverse network between the nodes (vertices). This network is called an Artificial Neural Network and is influenced by the neural network of the human brain. ANNs are used to draw conclusions about data in a way similar to how the human brain is anticipated to do so.

The neural network can also be considered to be a network of several individual decision trees. This data structure can be used in applications such as reasoning systems - where it's not just the results that matter but also the logic/reason behind it. 

<b>It should be noted that there are two kinds of learning mechanisms: supervised (from labeled dataset) and unsupervised (from unlabeled dataset).</b>

<br/><br/>

# Reinforcement Learning
This is another technique of making the computer learn, but not exactly from data. In this approach, the machine is given the capabilities to perform some fundamental actions, and a defined goal that it has to achieve. Now the machine tries out several permutations of its fundamental capabilities. If a certain permutation leads to the achievement of the goal, the machine is <b>rewarded points</b>, and it <b>learns</b> one of the ways to achieve the task. Whenever the machine fails to get to its goal, <b>points are deducted</b> so as to make it understand that the method did not work out.<br><br/>
A great example would be the AI used in games which learns to defeat the user. Deep learning and reinforcement learning have been used in combination to make computers learn to play games like Chess, Space Invaders, Jeopardy, etc.<br/><br/>  
Read [this paper](http://cs229.stanford.edu/notes/cs229-notes12.pdf) to have a deeper understanding how RL works. You can also checkout this [repository](https://github.com/ACM-VIT/awesome-Artificial-Intelligence/blob/master/Reinforcement%20Learning/Reinforcement%20Learning.ipynb)
<br/>  

# Artificial Neural Networks
Artificial Neural Networks are inspired by the human brain. The brain has a network of millions of neurons where each neuron (in a sub-network) gives an input and the final decision is a weighted sum of the inputs of the individual neurons.   
<br/>
<img src="https://proxy.duckduckgo.com/iu/?u=https%3A%2F%2Ftgmstat.files.wordpress.com%2F2013%2F05%2Fmulticlass_neural_network_example.png"/><br/>
Below is an illustration of a real life decision making process through a neural network.<br/>
<img src="https://i.imgur.com/tP5TQhu.png"/><br/>  

There are different types of neural networks based on how they analyse and interpret the data to form decision making nodes. The most common ones are <a href="https://en.wikipedia.org/wiki/Convolutional_neural_network">convolutional neural networks (CNN)</a> and <a href="https://en.wikipedia.org/wiki/Recurrent_neural_network">recurrent neural network (RNN)</a>. A complete list is available <a href="https://en.wikipedia.org/wiki/Types_of_artificial_neural_networks">here</a>.<br/><br/><br/>

# Image Processing
You must have used face or fingerprint recognition systems on phones and laptops. The form of data in which the face and fingerprint are captured is <b>image</b>. As you must have already guessed, making a computer recognize faces, fingerprints and other objects in an image is categorized as <b>Image processing</b>. Image processing can include methods ranging from simple matrix operations (since an image is a 2D matrix/array of pixels) to transforming the pixel data in a numerical form and feeding into neural networks. Recognition tasks may or may not need the use of neural networks depending on the complexity of the task. Most face recognition systems use neural networks.<br/><br/><br/>  

# Natural Language Processing
NLP is the process of analysing textual data (sentences in natural/human language).  Its application is very evident in voice assistant apps that exist on almost all smartphones and laptops. <b>Chat bots</b> are also a good example of NLP, though the most classic example is <b>grammar checker</b>.<br><br/>
Natural Language processing is used in <b>speech recognition</b>, which is different from <b>voice recognition</b>. Speech recognition means the identification of a command given by the user, whereas voice recognition is used to verify a user. Neural Networks are also used in NLP. In such cases, however, the text has to be <b>encoded</b> in a numerical form for processing.<br/><br/><br/>

# Audio Processing
It is more of a <b>data-fetching</b> technique than an entire domain of AI. The (analog) audio that is recorded has data like frequency, amplitude and wavelength. This data cannot directly be processed in a real world content using a computer. Audio processing involves the conversion of the analog data into discrete values which are nothing but numerical values which can be used for computation.<br/><br/>
Although the recognition part is done by neural networks, voice recognition systems are non-functional without a source for audio.
