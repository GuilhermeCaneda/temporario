import { useState } from 'react'
import './Home.css'
import axios from 'axios';

function Home() {

    const [nome, setNome] = useState('');
    const [cpf, setCpf] = useState('');
    const [respostaCPF, setRespostaCPF] = useState([]);
    //const [respostaCNPJ, setRespostaCNPJ] = useState([])


    const handleNome = (event) => {
        setNome(event.target.value);
    };
    const handleCpf = (event) => {
        setCpf(event.target.value);
    };

    const handleBuscarNome = () => {
        console.log("Pesquisando...")
        axios.get(`http://localhost:5000/name?name=${nome}`) 
            .then(response => {
                console.log(response.data)
                setRespostaCPF(response.data);
            })
            .catch(error => {
                console.error('Erro:', error);
            });
    }

    const handleBuscarNomeSimilar = () => {
        console.log("Pesquisando...")
        axios.get(`http://localhost:5000/similar_name?name=${nome}`) 
            .then(response => {
                console.log(response.data)
                setRespostaCPF(response.data);
            })
            .catch(error => {
                console.error('Erro:', error);
            });
    }

    const handleBuscarCpf = () => {
        console.log("Pesquisando...")
        axios.get(`http://localhost:5000/cpf?cpf=${cpf}`) 
            .then(response => {
                console.log(response.data)
                setRespostaCPF(response.data);
            })
            .catch(error => {
                console.error('Erro:', error);
            });
    }
    /*const handleBuscarCnpj = () => {
        setRespostaCPF([]);
        axios.get(`http://`) //MUDAR AQUI A ROTA
            .then(response => {
                setRespostaCNPJ(response.data);
            })
            .catch(error => {
                console.error('Erro:', error);
            });
    }*/


    /*
    <div className='socios-basecnpj'>
                {respostaCNPJ.length > 0 ? respostaCNPJ.map((item)  => (
                    <div onClick={handleBuscarCnpj} key={item[0]} className='socio-basecnpj'>
                        <h3>Radical:{item[0]} </h3>
                        <h3>Tipo: {item[1]}</h3>
                        <h3>Nome: {item[2]}</h3>
                        <h3>Cpf: {item[3]}</h3>
                        <h3>Qualificação: {item[4]}</h3>
                        <h3>Data: {item[5]}</h3>
                        <h3>Pais: {item[6]}</h3>
                        <h3>Representante Legal: {item[7]}</h3>
                        <h3>Nome do representante: {item[8]}</h3>
                        <h3>Qualificação do representante: {item[9]}</h3>
                        <h3>Faixa etária: {item[10]}</h3>
                    </div>
                )) : (<p>Nenhum foi encontrada.</p>)}
            </div>*/
    return (
        <div className='homecss'>
            <input placeholder="name" onChange={handleNome}/>
            <input placeholder="cpf" onChange={handleCpf}/>
            <button onClick={handleBuscarNome}>Buscar por nome</button>
            <button onClick={handleBuscarNomeSimilar}>Buscar por nome similar</button>
            <button onClick={handleBuscarCpf}>Buscar por cpf</button>

            <div className='pessoas-basecpf'>
                {respostaCPF.length > 0 ? respostaCPF.map((item) => (
                    <div key={item[0]} className='pessoa-basecpf'>
                        <h3>Nome: {item.nome}</h3>
                        <h3>Cpf: {item.cpf}</h3>
                        <h3>Sexo: {item.sexo}</h3>
                        <h3>Data: {item.nasc}</h3>
                    </div>
                )) : (<p>Nenhuma pessoa foi encontrada.</p>)}
            </div>

            

        </div>
    )
}

export default Home