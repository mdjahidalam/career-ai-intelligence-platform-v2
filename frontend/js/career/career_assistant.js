// ==========================================
// Career AI Assistant
// ==========================================

const API_BASE_URL =
    "http://127.0.0.1:8000";


// ==========================================
// DOM Elements
// ==========================================

const chatInput =
    document.getElementById(
        "chatInput"
    );

const sendMessageButton =
    document.getElementById(
        "sendMessageButton"
    );

const chatMessages =
    document.getElementById(
        "chatMessages"
    );

const newChatButton =
    document.getElementById(
        "newChatButton"
    );

const chatHistoryList =
    document.getElementById(
        "chatHistoryList"
    );


// ==========================================
// State
// ==========================================

let currentConversationId = null;

let conversations = [];


// ==========================================
// Token
// ==========================================

function getToken() {

    return localStorage.getItem(
        "access_token"
    );

}


// ==========================================
// Add Message
// ==========================================
// ==========================================
// Add Message
// ==========================================

function addMessage(
    message,
    type
) {

    const messageElement =
        document.createElement(
            "div"
        );


    // ==========================================
    // User Message
    // ==========================================

    if (type === "user") {

        messageElement.className =
            "user-message";

        messageElement.textContent =
            message;

    }


    // ==========================================
    // AI Message
    // ==========================================

    else {

        messageElement.className =
            "ai-message";

        messageElement.innerHTML =
            marked.parse(message);

    }


    chatMessages.appendChild(
        messageElement
    );

    scrollToBottom();

}


// ==========================================
// Loading Message
// ==========================================

function showLoadingMessage() {

    const loading =
        document.createElement(
            "div"
        );

    loading.id =
        "aiLoadingMessage";

    loading.className =
        "ai-message";

    loading.textContent =
        "Thinking...";

    chatMessages.appendChild(
        loading
    );

    scrollToBottom();

}


function removeLoadingMessage() {

    const loading =
        document.getElementById(
            "aiLoadingMessage"
        );

    if (loading) {

        loading.remove();

    }

}


// ==========================================
// Scroll
// ==========================================

function scrollToBottom() {

    chatMessages.scrollTop =
        chatMessages.scrollHeight;

}


// ==========================================
// New Conversation
// ==========================================

function createNewConversation() {

    currentConversationId = null;

    chatMessages.innerHTML = "";

    addWelcomeMessage();

    renderHistory();

    chatInput.focus();

}


// ==========================================
// Clear Chat
// ==========================================

function clearChat() {

    chatMessages.innerHTML = "";

    addWelcomeMessage();

}


// ==========================================
// Welcome Message
// ==========================================

function addWelcomeMessage() {

    const messageElement =
        document.createElement(
            "div"
        );

    messageElement.className =
        "ai-message";

    messageElement.innerHTML = `

        Hello! I'm your
        <strong>
            Career AI Assistant
        </strong>.

        <br><br>

        I can help you with:

        <ul>

            <li>
                Career guidance
            </li>

            <li>
                Learning and technical concepts
            </li>

            <li>
                Interview preparation
            </li>

            <li>
                Mock interviews
            </li>

            <li>
                Job preparation
            </li>

        </ul>

        What would you like to work on today?

    `;

    chatMessages.appendChild(
        messageElement
    );

}

// ==========================================
// Send Message - SSE Streaming
// ==========================================

async function sendMessage() {

    const message =
        chatInput.value.trim();

    if (!message) {
        return;
    }


    // ==========================================
    // Show User Message
    // ==========================================

    addMessage(
        message,
        "user"
    );

    chatInput.value = "";

    sendMessageButton.disabled = true;


    // ==========================================
    // Create Empty AI Message
    // ==========================================

    const aiMessageElement =
        createStreamingMessage();


    let fullResponse = "";


    try {

        // ==========================================
        // Streaming Request
        // ==========================================

        const response =
            await fetch(

                API_BASE_URL +
                "/career/chat/stream",

                {

                    method: "POST",

                    headers: {

                        "Content-Type":
                            "application/json",

                        "Authorization":
                            "Bearer " +
                            getToken()

                    },

                    body: JSON.stringify({

                        conversation_id:
                            currentConversationId,

                        message:
                            message

                    })

                }

            );


        // ==========================================
        // HTTP Error
        // ==========================================

        if (!response.ok) {

            let errorMessage =
                "Unable to get AI response.";

            try {

                const errorData =
                    await response.json();

                errorMessage =
                    errorData.detail ||
                    errorMessage;

            }
            catch {

                // Ignore JSON parsing error

            }

            throw new Error(
                errorMessage
            );

        }


        if (!response.body) {

            throw new Error(
                "Streaming is not supported."
            );

        }


        // ==========================================
        // Read Stream
        // ==========================================

        const reader =
            response.body.getReader();

        const decoder =
            new TextDecoder();

        let buffer = "";


        while (true) {

            const {
                value,
                done
            } =
                await reader.read();


            if (done) {
                break;
            }


            buffer +=
                decoder.decode(
                    value,
                    {
                        stream: true
                    }
                );


            // ==========================================
            // Split SSE Events
            // ==========================================

            const events =
                buffer.split("\n\n");


            // Keep incomplete event
            buffer =
                events.pop();


            for (
                const eventText
                of events
            ) {

                const result =
                    processSSEEvent(
                        eventText
                    );


                if (!result) {
                    continue;
                }


                // ==========================================
                // Conversation Created
                // ==========================================

                if (
                    result.event ===
                    "conversation"
                ) {

                    if (result.data.id) {

                        currentConversationId =
                            result.data.id;

                    }

                }


                // ==========================================
                // AI Chunk
                // ==========================================

                if (
                    result.event ===
                    "chunk"
                ) {

                    const content =
                        result.data.content ||
                        "";


                    if (content) {

                        fullResponse +=
                            content;


                        updateStreamingMessage(

                            aiMessageElement,

                            fullResponse

                        );

                    }

                }


                // ==========================================
                // Conversation Updated
                // ==========================================

                if (
                    result.event ===
                    "conversation_updated"
                ) {

                    if (result.data.id) {

                        currentConversationId =
                            result.data.id;

                    }


                    if (result.data.title) {

                        let conversation =
                            conversations.find(

                                item =>
                                    item.id ===
                                    result.data.id

                            );


                        if (conversation) {

                            conversation.title =
                                result.data.title;

                        }

                    }

                }


                // ==========================================
                // Error
                // ==========================================

                if (
                    result.event ===
                    "error"
                ) {

                    throw new Error(

                        result.data.message ||
                        "AI streaming failed."

                    );

                }

            }

        }


        // ==========================================
        // Process Remaining Buffer
        // ==========================================

        buffer +=
            decoder.decode();


        if (buffer.trim()) {

            const result =
                processSSEEvent(
                    buffer
                );


            if (result) {

                if (
                    result.event ===
                    "chunk"
                ) {

                    const content =
                        result.data.content ||
                        "";

                    fullResponse +=
                        content;

                }


                if (
                    result.event ===
                    "conversation"
                ) {

                    if (result.data.id) {

                        currentConversationId =
                            result.data.id;

                    }

                }

            }

        }


        // ==========================================
        // Validate
        // ==========================================

        if (!fullResponse.trim()) {

            throw new Error(
                "No response received."
            );

        }


        // ==========================================
        // Store Conversation Locally
        // ==========================================

        let conversation =
            conversations.find(

                item =>
                    item.id ===
                    currentConversationId

            );


        if (!conversation) {

            conversation = {

                id:
                    currentConversationId,

                title:
                    message.length > 35
                        ? message.substring(
                            0,
                            35
                        ) + "..."
                        : message,

                messages: [],

                created_at:
                    new Date().toISOString(),

                updated_at:
                    new Date().toISOString()

            };

            conversations.push(
                conversation
            );

        }


        // ==========================================
        // Store User Message
        // ==========================================

        conversation.messages.push({

            role: "user",

            content:
                message

        });


        // ==========================================
        // Store AI Message
        // ==========================================

        conversation.messages.push({

            role: "assistant",

            content:
                fullResponse

        });


        // ==========================================
        // Final Markdown Rendering
        // ==========================================

        updateStreamingMessage(

            aiMessageElement,

            fullResponse,

            true

        );


        // ==========================================
        // Update History
        // ==========================================

        await loadChatHistory();


        updateConversationTitle(
            message
        );


    }
    catch (error) {

        console.error(
            "Career AI streaming error:",
            error
        );


        aiMessageElement.textContent =
            "Sorry, something went wrong. Please try again.";

    }


    finally {

        sendMessageButton.disabled =
            false;

        chatInput.focus();

    }

}
// ==========================================
// Process SSE Event
// ==========================================

function processSSEEvent(
    eventText
) {

    if (!eventText.trim()) {
        return null;
    }


    let eventName =
        "message";

    let dataText =
        "";


    const lines =
        eventText.split(/\r?\n/);


    for (
        const line
        of lines
    ) {

        if (
            line.startsWith("event:")
        ) {

            eventName =
                line
                    .substring(6)
                    .trim();

        }


        else if (
            line.startsWith("data:")
        ) {

            dataText +=
                line
                    .substring(5)
                    .trim();

        }

    }


    if (!dataText) {
        return null;
    }


    let data;


    try {

        data =
            JSON.parse(
                dataText
            );

    }
    catch (error) {

        console.error(
            "Invalid SSE JSON:",
            dataText
        );

        return null;

    }


    return {

        event:
            eventName,

        data:
            data

    };

}
// ==========================================
// Create Streaming AI Message
// ==========================================

function createStreamingMessage() {

    const messageElement =
        document.createElement(
            "div"
        );


    messageElement.className =
        "ai-message";


    messageElement.textContent =
        "";


    chatMessages.appendChild(
        messageElement
    );


    scrollToBottom();


    return messageElement;

}


// ==========================================
// Update Streaming AI Message
// ==========================================

function updateStreamingMessage(

    messageElement,

    content,

    final = false

) {

    if (
        final &&
        typeof marked !== "undefined"
    ) {

        messageElement.innerHTML =
            marked.parse(
                content
            );

    }
    else {

        messageElement.textContent =
            content;

    }


    scrollToBottom();

}

// ==========================================
// Update Conversation Title
// ==========================================

function updateConversationTitle(
    message
) {

    const conversation =
        conversations.find(

            item =>
                item.id ===
                currentConversationId

        );


    if (!conversation) {

        return;

    }


    if (
        conversation.title ===
        "New Conversation"
    ) {

        conversation.title =
            message.length > 35
                ? message.substring(
                    0,
                    35
                ) + "..."
                : message;

        renderHistory();

    }

}


// ==========================================
// Load Chat History From Backend
// ==========================================

async function loadChatHistory() {

    try {

        const response = await fetch(

            API_BASE_URL +
            "/career/history",

            {
                method: "GET",

                headers: {
                    "Authorization":
                        "Bearer " + getToken()
                }
            }

        );


        const data =
            await response.json();


        if (!response.ok) {

            throw new Error(

                data.detail ||
                "Unable to load chat history."

            );

        }


        conversations =
            (data.data || []).map(

                conversation => ({

                    id:
                        conversation.id,

                    title:
                        conversation.title ||
                        "New Conversation",

                    messages: [],

                    created_at:
                        conversation.created_at,

                    updated_at:
                        conversation.updated_at

                })

            );


        renderHistory();


    }
    catch (error) {

        console.error(
            "Failed to load chat history:",
            error
        );

    }

}
// ==========================================
// Get History Date Group
// ==========================================

function getHistoryGroup(dateString) {

    const chatDate =
        new Date(dateString);

    const now =
        new Date();


    // Today 00:00:00
    const today =
        new Date(
            now.getFullYear(),
            now.getMonth(),
            now.getDate()
        );


    // Yesterday 00:00:00
    const yesterday =
        new Date(today);

    yesterday.setDate(
        yesterday.getDate() - 1
    );


    // Previous 7 days
    const previousSevenDays =
        new Date(today);

    previousSevenDays.setDate(
        previousSevenDays.getDate() - 7
    );


    if (chatDate >= today) {

        return "Today";

    }


    if (chatDate >= yesterday) {

        return "Yesterday";

    }


    if (chatDate >= previousSevenDays) {

        return "Previous 7 Days";

    }


    return "Older";

}


// ==========================================
// Render Chat History
// ==========================================

function renderHistory() {

    chatHistoryList.innerHTML = "";


    if (
        conversations.length === 0
    ) {

        return;

    }


    // ==========================================
    // Create Groups
    // ==========================================

    const groups = {

        "Today": [],

        "Yesterday": [],

        "Previous 7 Days": [],

        "Older": []

    };


    // ==========================================
    // Put Conversations Into Groups
    // ==========================================

    conversations.forEach(

        conversation => {

            const date =
                conversation.updated_at ||
                conversation.created_at;


            const groupName =
                getHistoryGroup(date);


            groups[groupName].push(
                conversation
            );

        }

    );


    // ==========================================
    // Group Order
    // ==========================================

    const groupOrder = [

        "Today",

        "Yesterday",

        "Previous 7 Days",

        "Older"

    ];


    // ==========================================
    // Render Groups
    // ==========================================

    groupOrder.forEach(

        groupName => {

            const chats =
                groups[groupName];


            // No chats in this group
            if (
                chats.length === 0
            ) {

                return;

            }


            const group =
                document.createElement(
                    "div"
                );

            group.className =
                "history-group";


            // ==========================================
            // Group Heading
            // ==========================================

            const date =
                document.createElement(
                    "div"
                );

            date.className =
                "history-date";

            date.textContent =
                groupName;


            group.appendChild(
                date
            );


            // ==========================================
            // Sort Newest First
            // ==========================================

            chats
                .slice()
                .sort(

                    (a, b) => {

                        const dateA =
                            new Date(
                                a.updated_at ||
                                a.created_at
                            );

                        const dateB =
                            new Date(
                                b.updated_at ||
                                b.created_at
                            );

                        return dateB - dateA;

                    }

                )
                .forEach(

                    conversation => {

                        const historyItem =
                            document.createElement(
                                "div"
                            );

                        historyItem.className ="history-item-wrapper";

                        const button =
                                document.createElement(
                                     "button"
                                );
                        button.type =
                            "button";


                        button.className =
                            "history-item";


                        // ==========================================
                        // Active Conversation
                        // ==========================================

                        if (
                            conversation.id ===
                            currentConversationId
                        ) {

                            button.classList.add(
                                "active"
                            );

                        }


                        button.textContent =
                            conversation.title;
                        
                        // ==========================================
                        // More Button
                        // ==========================================

                        const moreButton =
                            document.createElement(
                                "button"
                            );

                        moreButton.type =
                            "button";

                        moreButton.className =
                            "history-more";

                        moreButton.textContent ="⋮";


                        moreButton.addEventListener("click",
                            function (event) {

                                event.stopPropagation();

                                showChatActions(
                                    conversation.id,
                                    moreButton
                                );

                            }
                        );


                        // ==========================================
                        // Open Conversation
                        // ==========================================

                        button.addEventListener(

                            "click",

                            function () {

                                openConversation(
                                    conversation.id
                                );

                            }

                        );


                        historyItem.appendChild(
                            button
                        );
                        historyItem.appendChild(
                            moreButton
                        );

                        group.appendChild(
                            historyItem
                        );

                    }

                );


            chatHistoryList.appendChild(
                group
            );

        }

    );

}

// ==========================================
// Rename Conversation
// ==========================================

async function renameConversation(
    conversationId
) {

    const conversation =
        conversations.find(
            item =>
                item.id === conversationId
        );


    if (!conversation) {
        return;
    }


    const newTitle =
        prompt(
            "Enter new chat title:",
            conversation.title
        );


    if (!newTitle) {
        return;
    }


    const trimmedTitle =
        newTitle.trim();


    if (!trimmedTitle) {
        return;
    }


    try {

        const response =
            await fetch(

                API_BASE_URL +
                `/career/history/${conversationId}/rename`,

                {
                    method: "PUT",

                    headers: {

                        "Content-Type":
                            "application/json",

                        "Authorization":
                            "Bearer " +
                            getToken()

                    },

                    body: JSON.stringify({

                        title:
                            trimmedTitle

                    })

                }

            );


        const data =
            await response.json();


        if (!response.ok) {

            throw new Error(

                data.detail ||
                "Unable to rename conversation."

            );

        }


        conversation.title =
            data.data.title;


        renderHistory();


    }
    catch (error) {

        console.error(
            "Rename conversation error:",
            error
        );

        alert(
            "Unable to rename conversation."
        );

    }

}



// ==========================================
// Chat Actions Dropdown
// ==========================================

function showChatActions(
    conversationId,
    button
) {

    // Remove existing menu
    const oldMenu =
        document.querySelector(
            ".chat-actions-menu"
        );

    if (oldMenu) {
        oldMenu.remove();
    }


    // ==========================================
    // Create Menu
    // ==========================================

    const menu =
        document.createElement(
            "div"
        );

    menu.className =
        "chat-actions-menu";


    // ==========================================
    // Rename Button
    // ==========================================

    const renameButton =
        document.createElement(
            "button"
        );

    renameButton.type =
        "button";

    renameButton.className =
        "chat-action-button";

    renameButton.innerHTML =
        "✏️ Rename";


    renameButton.addEventListener(
        "click",
        function (event) {

            event.stopPropagation();

            menu.remove();

            renameConversation(
                conversationId
            );

        }
    );


    // ==========================================
    // Delete Button
    // ==========================================

    const deleteButton =
        document.createElement(
            "button"
        );

    deleteButton.type =
        "button";

    deleteButton.className =
        "chat-action-button delete-action";

    deleteButton.innerHTML =
        "🗑️ Delete";


    deleteButton.addEventListener(
        "click",
        function (event) {

            event.stopPropagation();

            menu.remove();

            deleteConversation(
                conversationId
            );

        }
    );


    // ==========================================
    // Add Buttons
    // ==========================================

    menu.appendChild(
        renameButton
    );

    menu.appendChild(
        deleteButton
    );


    // ==========================================
    // Position Menu
    // ==========================================

    const rect =
        button.getBoundingClientRect();


    menu.style.position =
        "fixed";

    menu.style.top =
        `${rect.bottom + 4}px`;

    menu.style.left =
        `${rect.left - 110}px`;


    document.body.appendChild(
        menu
    );


    // ==========================================
    // Close When Clicking Outside
    // ==========================================

    setTimeout(
        function () {

            document.addEventListener(
                "click",
                closeChatActionsMenu,
                {
                    once: true
                }
            );

        },
        0
    );

}


// ==========================================
// Close Chat Actions Menu
// ==========================================

function closeChatActionsMenu() {

    const menu =
        document.querySelector(
            ".chat-actions-menu"
        );

    if (menu) {

        menu.remove();

    }

}
// ==============================
// Open Conversation
// ==========================================

async function openConversation(
    conversationId
) {

    try {

        currentConversationId =
            conversationId;


        chatMessages.innerHTML = "";


        showLoadingMessage();


        const response = await fetch(

            API_BASE_URL +
            "/career/history/" +
            conversationId,

            {
                method: "GET",

                headers: {
                    "Authorization":
                        "Bearer " + getToken()
                }
            }

        );


        const data =
            await response.json();


        if (!response.ok) {

            throw new Error(

                data.detail ||
                "Unable to load conversation."

            );

        }


        removeLoadingMessage();


        const conversationData =
            data.data;


        // ==========================================
        // Find Local Conversation
        // ==========================================

        let conversation =
            conversations.find(

                item =>
                    item.id ===
                    conversationId

            );


        if (!conversation) {

            conversation = {

                id: conversationData.id,

                title:
                    conversationData.title,

                messages: []

            };

            conversations.push(
                conversation
            );

        }


        // ==========================================
        // Store Messages Locally
        // ==========================================

        conversation.messages =
            conversationData.messages.map(
                message => ({

                    role:
                        message.role,

                    content:
                        message.message

                })
            );


        conversation.title =
            conversationData.title;


        // ==========================================
        // Display Messages
        // ==========================================

        if (
            conversation.messages.length ===
            0
        ) {

            addWelcomeMessage();

        } else {

            conversation.messages.forEach(

                message => {

                    addMessage(

                        message.content,

                        message.role === "user"
                            ? "user"
                            : "ai"

                    );

                }

            );

        }


        renderHistory();

        scrollToBottom();


    } catch (error) {

        console.error(
            "Open conversation error:",
            error
        );


        removeLoadingMessage();


        chatMessages.innerHTML = "";


        addMessage(
            "Unable to load this conversation. Please try again.",
            "ai"
        );

    }

}


// ==========================================
// Events
// ==========================================

sendMessageButton.addEventListener(

    "click",

    sendMessage

);


chatInput.addEventListener(

    "keydown",

    function (event) {

        if (

            event.key ===
                "Enter" &&
            !event.shiftKey

        ) {

            event.preventDefault();

            sendMessage();

        }

    }

);


newChatButton.addEventListener(

    "click",

    createNewConversation

);


// ==========================================
// Initial State
// ==========================================

// ==========================================
// Initial Page Load
// ==========================================

currentConversationId = null;

chatMessages.innerHTML = "";

addWelcomeMessage();

loadChatHistory();