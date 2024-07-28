
    let certificateCounter = 0;
    function addCertificateInput(){
        //let certiCounter = 0;
        if(certificateCounter <= 9){
            let inpuWrapper = document.getElementById('certificate-input-wrapper');
            let newInput = document.createElement('div');
            newInput.classList.add('input-group', 'mt-3');

            let fileInput = document.createElement('input');
            fileInput.type = 'file';
            fileInput.name = 'certificate_files';
            fileInput.classList.add('custom-file-input');
            fileInput.multiple = true;

            let customFileLabel = document.createElement('label');
            customFileLabel.classList.add('custom-file-label');
            customFileLabel.setAttribute('for', 'customFile');

            fileInput.addEventListener('change', function() {
                let fileName = Array.from(this.files).map(file => file.name).join(', ');
                customFileLabel.textContent = fileName;
            });

            // Delete button
            let removeButton = document.createElement('button');
            removeButton.textContent = 'Remove';
            removeButton.type = 'button';
            removeButton.classList.add('btn', 'btn-danger');

            removeButton.addEventListener('click', function(){
                inputWarapper.removeChild(newInput);
                certiCounter--;
            });

            let customFileDiv = document.createElement('div');
            customFileDiv.classList.add('custom-file');
            customFileDiv.appendChild(fileInput);
            customFileDiv.appendChild(customFileLabel);

            let inputGroupAppend = document.createElement('div');
            inputGroupAppend.classList.add('input-group-append');
            inputGroupAppend.appendChild(removeButton);

            newInput.appendChild(customFileDiv);
            newInput.appendChild(inputGroupAppend);
            inputWarapper.appendChild(newInput);
            certiCounter++;
        }
    }
