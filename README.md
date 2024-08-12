# comfyui-selector
 
> Quick and dirty nodes for [ComfyUI](https://github.com/comfyanonymous/comfyui)
> 
> The nodes will be listed under images/utils, or you can type ```.``` to find it in search/double-click menu on the grid. 
 
> [!Note]
> 注釋
>  ```git clone https://github.com/exdysa/comfyui-selector/```
> 或將.py檔案放在...內 or place [the .py file](https://raw.githubusercontent.com/exdysa/comfyui-selector/main/selector.py) inside `custom_nodes`.

> "資源"節點 - 從python-goss/ltdrdata建立。如果輸入被静音/跳過/刪除，它使用'fallback'中的替代輸入。這裡還有一個額外的布林出口，你可以在邏輯混亂中使用它。請確保輸入、失敗和輸出類型相符...
> "Recourse" node - building from pythongoss/ltdrdata. If the input has been muted/bypassed/deleted, it uses the alternative input in 'fallback'. There is an additional boolean out that you can use for logic mayhem as well. You _probably_ want to make sure input, fallback and output types match...
>
> ![Screenshot 2024-06-04 020106](https://github.com/exdysa/comfyui-selector/assets/91800957/172c57c4-48a6-41b2-aad7-c7ce1240a2f7)

> "資源"現在有6個fallback朋友，大部分都由一個模式識別節點稱為Check控制，並根據檢查點類型重新導向輸出。輸入1是sd，2是xl，3是sd3，而輸入4是refiner。這大大簡化了自動化任務。
> "Recourse" now has 6 fallback friends, most of which are controlled by a model-identifying node called Check that redirects output based on checkpoint type. input 1 is sd, 2 is xl, 3 is sd3 and input 4 is refiner. This greatly simplifies automation tasks.
> ![recoursecheck](https://github.com/exdysa/comfyui-selector/assets/91800957/be002cf1-b597-4b1d-8d3e-cc30d666087f)
> ![forkmodel](https://github.com/exdysa/comfyui-selector/assets/91800957/fabb71ef-7092-4b43-b2a8-e64555cf7381)
> ![forkclip](https://github.com/exdysa/comfyui-selector/assets/91800957/f6e24932-6e69-4853-9dcf-1c01383764ae)
> ![unite](https://github.com/exdysa/comfyui-selector/assets/91800957/eeb58b34-e99d-409c-b862-1f5f7dfd21e1)
> ![recoursepolar](https://github.com/exdysa/comfyui-selector/assets/91800957/ab2fe0a9-cd5f-48dd-8c38-8f281f62ce15)
> ![recourseimg](https://github.com/exdysa/comfyui-selector/assets/91800957/1c8dc87f-dcac-41ba-b625-7386fb9f7a9d)

> "選擇器"節點 - 生成用於其他節點的簡單參數  "Selector" node - Generates simple parameters to use in other nodes
> ![Screenshot_2024-05-26_16-12-36](https://github.com/exdysa/comfyui-selector/assets/91800957/fbba564f-b4df-48fc-8489-f01dc60bc8ba)
> ![Screenshot_2024-05-26_17-44-08](https://github.com/exdysa/comfyui-selector/assets/91800957/30ed648b-802b-474c-a48c-371813d6d102)
> ![Screenshot_2024-05-26_16-13-26](https://github.com/exdysa/comfyui-selector/assets/91800957/2dd842b5-f84b-423d-b430-bd85e19e9e33)
> 
> Data output todo :
> - ~SD 3.0 resolutions~
> - ~sampler options~
> - ~support for Pixart alpha/sigma, playground, kandinsky, etc...~
> - ~upscale dimensions and factors~
> - ~multiple steps~
> - ~multiple cfgs~
> - ~refiner steps~
> - ~multiple denoises~
> - ~...toast??~

> Initial plans I will likely not attempt :
> - custom values
> - multiple seeds
> - nested menus for model types
