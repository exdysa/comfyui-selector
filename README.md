# comfyui-selector

>
ComfyUI-Selector擴充套件節點透過識別模型和向其他節點廣播設定來增強ComfyUI。 這些訊號在節點圖中同時更改了許多節點的設定，使使用者從技術工作中解放出來，這樣他們就可以專注於ComfyUI中的藝術體驗。

在您的指揮下，有十五個功能強大且易於理解的節點。 “Recourse”節點透過提供輔助訊號來防止連線中斷。 現在，您可以減少因錯誤而中斷工作的頻率。“Selector”根據模型指導節點的訊號流。 建立精確而靈活的工作流程，這些工作流程可以像您的靈感一樣快速發展。

感謝您的下載。 請期待它。

## Installation:
> 自動安裝從[ComfyUI-Manager](https://github.com/ltdrdata/ComfyUI-Manager)
>
> or
>
>  ```git clone https://github.com/exdysa/comfyui-selector/```
>
> or
>
> 或將.py檔案放在...內 `custom_nodes`.

## Usage:

> “Selector” : 在這裡為許多節點選擇選項
> - 水平維度,  垂直維度.一次要製作的影象數量,迭代,詳細步驟,CFG, Detailer CFG, denoise...

> “Recourse” :在發生事故時新增二級模型
> - 活動自動用於每個輸入。 連線許多相同型別的。 安全第一！

> “Selector In/Out”: 添加 “model_type”. 輸出是模型的編號如下：
> - 1 STABLE DIFFUSION 1
> - 2 STABLE DIFFUSION XL
> - 3 FLUX
> - 4 AURAFLOW
> - 5 HUNYUANDIT
> - 6 STABLE DIFFUSION 3
> - 7 STABLE CASCADE-C
> - 8 STABLE CASCADE-B

<hr>
ComfyUI-Selector extension node enhances ComfyUI by identifying models and broadcasting to other nodes. These signals change the settings of many nodes in the node diagram at the same time, freeing users from technical work, so that they can focus on the artistic experience in ComfyUI.

Under your command are fifteen powerful and easy-to-understand nodes:

- The "Recourse" node prevents connection interruption by providing auxiliary signals. Now, you can reduce the frequency of interruptions due to errors.

- Selector" guides the signal flow of the node according to the model. Create accurate and flexible workflows, which can develop as quickly as your inspiration.

 ## Installation:
 > Automatic installation from [ComfyUI-Manager](https://github.com/ltdrdata/ComfyUI-Manager)
 >
 > or
 >
 > ```git clone https://github.com/exdysa/comfyui-selector/```
 >
 > or
 > put the .py file in... Inside `custom_nodes`.

 ## Usage:

 > - "Selector": Select options for many nodes here
 > - horizontal dimension, vertical dimension. The number of images to be produced at a time, iteration, detailed steps, CFG, Detailer CFG, denoise, etc

 > -"Recourse": Add a secondary model.
 > In the event of an accident, automatically uses an active input. Connect many of the same type. Safety first!

> "Selector In/Out": Add "model_type". The output is the number of the model as follows:
> - 1 STABLE DIFFUSION 1
> - 2 STABLE DIFFUSION XL
> - 3 FLUX
> - 4 AURAFLOW
> - 5 HUNYUANDIT
> - 6 STABLE DIFFUSION 3
> - 7 STABLE CASCADE-C
> - 8 STABLE CASCADE-B

