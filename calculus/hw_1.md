## Тема “Введение в математических анализ”

1. **Как относятся друг к другу множество и последовательность? (в ответе использовать слова типа: часть, целое, общее, частное, родитель, дочерний субъект и т.д.)**

 Множество символизирует объект, сам состоящий из других объектов (элементов), объединенных по одному признаку.

Последовательность - бесконечная выборка на упорядоченном множестве натуральных чисел. При этом каждому натуральному числу сопоставляется член последовательности (при этом натуральное число становится его номером или индексом).

Выборка - результат последовательного выбора элементов множества.

Получается, что последовательность – это результат бесконечного последовательного выбора элементов упорядоченного множества элементы которого пронумерованы натуральными числами. Следовательно последовательность – это множество, элементы которого последовательно пронумерованы.

**Правильный ответ**: Последовательность - отображение множества натуральных чисел: f:N→x Каждому натуральному числу соответствует элемент данного множества.



2. **Прочитать высказывания математической логики, построить их отрицания и установить истинность.**

2.1. ∀y ∈ [0;1] : sgn(y) = 1

  Для любых y принадлежащих множеству [0;1] сигнум от y равен 1. **Ложь**

  **Отрицание**: ∃y ∈ [0;1] : sgn(y) ≠ 1

  

2.2. ∀n ∈ N > 2 : ∃x,y,z ∈ ℕ : x<sup>n</sup> = y<sup>n</sup> + z<sup>n</sup>
  
  Для любых n принадлежащих множеству натуральным числам больше 2 существуют такие x, y, z принадлежащие натуральным числам, что x<sup>n</sup> = y<sup>n</sup> + z<sup>n</sup>  Это высказывание обратно теореме Ферма, которая утверждает  об отсутствии решений и доказанной в 1994 году Эндрю Уайлсом. **Ложь**

  **Отрицание**: ∃n ∈ N > 2 : ∀x,y,z ∈ ℕ : x<sup>n</sup> ≠ y<sup>n</sup> + z<sup>n</sup> 

  
  
2.3. ∀x ∈ ℝ∃X ∈ ℝ : X > x
  
  Для любых x принадлежащих множеству вещественных (рациональных) чисел существует X  принадлежащий вещественным (рациональным) числам такой что X > x. **Истина**

  **Отрицание**: ∃x ∈ ℝ:∀X ∈ ℝ | X ≠ x: X < x

  
  
2.4. ∀x ∈ ℂ∄y ∈ ℂ : x > y || x < y

  Для любых x принадлежащих множеству комплексных чисел не существует y принадлежащий множеству комплексных чисел такой что x > y или x < y. **Истина** т.к. комплексные числа не подлежат сравнению.

  **Отрицание**: ∃x, y ∈ ℂ : x ≤ y || x ≥ y

2.5. ∀y ∈ [0; π/2]∃ε > 0 : siny < sin(y+ε)

  Для любых y принадлежащих множеству [0;π/2] существует такое ε > 0, что siny < sin(y+ε). **Ложь** т.к. приращение угла даёт приращение синуса.

  **Отрицание**: ∃y ∈ [0; π/2]∀ε > 0 : siny ≥ sin(y+ε)

  

2.6. ∀y ∈ [0; π)∃ε > 0 : cosy > cos(y+ε)

  Для любых y принадлежащих множеству [0; π] существует такое ε > 0, что cosy > cos(y+ε). **Истина**

  **Отрицание**: ∃y ∈ [0; π)∀ε > 0 : cosy ≤ cos(y+ε)

  

2.7.  ∃x : x ∉ {ℕ, ℤ, ℚ, ℝ, ℂ}

  Существует такое x, которое не принадлежит множествам натуральных, целых, рациональных, вещественных (действительных) и комплексных чисел. **Истина** Таким числом может быть гиперкомплексное число.

  **Отрицание**: ∀x : x ∈ {ℕ, ℤ, ℚ, ℝ, ℂ}

  

## Тема “Последовательность”

1. **Даны 4 последовательности. Необходимо**:

 - **исследовать их на монотонность**; 
 - **исследовать на ограниченность**;
 - **найти пятый по счету член**.


  - {a<sub>n</sub>}<sup>∞</sup><sub>n=1</sub> = 2<sup>n</sup> - n   -  последовательность возрастает т. к. степенная функция растёт быстрее чем вычитаемая линейная. Члены последовательности принимают значения на интервале [1; +∞), следовательно последовательность **ограничена снизу**.
	
	 a<sub>5</sub> = 2<sup>5</sup> - 5 = 32 - 5 = **27**

  - {b<sub>n</sub>}<sup>∞</sup><sub>n=2</sub> = 1 / (1-n)   -  последовательность возрастает т. к. знаменатель увеличивается, но дробь получается отрицательной. Члены последовательности принимают значения на интервале (-∞; -1], следовательно последовательность **ограничена сверху**.

     Пятым по порядку элементом будет элемент под номером 6: b<sub>6</sub> = 1 / (1-6) = **-1/5**

  - {c<sub>n</sub>}<sup>∞</sup><sub>n=1</sub> = -1<sup>n</sup> +  sqrt(2n)  - последовательность возрастает т. к.  -1<sup>n</sup> принимает значения -1 и 1, а корень из 2n положительный и возрастает. Члены последовательности принимают значения на интервале [sqrt(2)-1; +∞), следовательно последовательность **ограниченна снизу**.

     c<sub>5</sub> = -1<sup>5</sup> + sqrt(2*5) = **sqrt(10) - 1**

  - {d<sub>n</sub>}<sup>∞</sup><sub>n=1</sub> = (-1)<sup>2n</sup> + 1/n<sup>2</sup>   - последовательность убывает. (-1)<sup>2n</sup> всегда в чётной степени и = 1. А 1/n<sup>2</sup> убывает т.к. знаменатель - растущая квадратичная функция. Члены последовательности принимают значения на интервале [2; 1,(1)), следовательно последовательность **ограниченна**.

     d<sub>5</sub> = -1<sup>10</sup> + 1/5<sup>2</sup> = 1 + 1/25 = **1.04**
     
     

2. **Найти 12-й член заданной неявно последовательности a<sub>1</sub> = 128, a<sub>n+1</sub> - a<sub>n</sub> = 6**.

   Элементы последовательности отличаются на 6 т. к. a<sub>n+1</sub> = a<sub>n</sub> + 6

   Т. к. нужно получить 12-й член последовательности, то к 1-му члену нужно прибавить ещё 11 членов, т. е:

   a<sub>12</sub> = a<sub>1</sub> + 11*6 = 128 + 66 = **194**
