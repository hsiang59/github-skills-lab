/**
 * 任務管理器範例
 * 展示如何使用 Copilot 建立簡單的任務管理應用
 */

class Task {
    constructor(id, title, description, priority = 'medium', completed = false) {
        this.id = id;
        this.title = title;
        this.description = description;
        this.priority = priority; // 'low', 'medium', 'high'
        this.completed = completed;
        this.createdAt = new Date();
        this.completedAt = null;
    }

    complete() {
        this.completed = true;
        this.completedAt = new Date();
    }

    uncomplete() {
        this.completed = false;
        this.completedAt = null;
    }
}

class TaskManager {
    constructor() {
        this.tasks = [];
        this.nextId = 1;
    }

    /**
     * 添加新任務
     * @param {string} title - 任務標題
     * @param {string} description - 任務描述
     * @param {string} priority - 優先級
     * @returns {Task} 新創建的任務
     */
    addTask(title, description, priority = 'medium') {
        const task = new Task(this.nextId++, title, description, priority);
        this.tasks.push(task);
        return task;
    }

    /**
     * 根據 ID 獲取任務
     * @param {number} id - 任務 ID
     * @returns {Task|null} 任務對象或 null
     */
    getTask(id) {
        return this.tasks.find(task => task.id === id) || null;
    }

    /**
     * 刪除任務
     * @param {number} id - 要刪除的任務 ID
     * @returns {boolean} 是否成功刪除
     */
    deleteTask(id) {
        const index = this.tasks.findIndex(task => task.id === id);
        if (index !== -1) {
            this.tasks.splice(index, 1);
            return true;
        }
        return false;
    }

    /**
     * 標記任務為已完成
     * @param {number} id - 任務 ID
     * @returns {boolean} 是否成功
     */
    completeTask(id) {
        const task = this.getTask(id);
        if (task) {
            task.complete();
            return true;
        }
        return false;
    }

    /**
     * 獲取所有未完成的任務
     * @returns {Array<Task>} 未完成的任務列表
     */
    getPendingTasks() {
        return this.tasks.filter(task => !task.completed);
    }

    /**
     * 獲取所有已完成的任務
     * @returns {Array<Task>} 已完成的任務列表
     */
    getCompletedTasks() {
        return this.tasks.filter(task => task.completed);
    }

    /**
     * 根據優先級獲取任務
     * @param {string} priority - 優先級 ('low', 'medium', 'high')
     * @returns {Array<Task>} 指定優先級的任務列表
     */
    getTasksByPriority(priority) {
        return this.tasks.filter(task => task.priority === priority);
    }

    /**
     * 獲取所有任務的統計資訊
     * @returns {Object} 統計資訊對象
     */
    getStatistics() {
        const total = this.tasks.length;
        const completed = this.getCompletedTasks().length;
        const pending = this.getPendingTasks().length;
        const byPriority = {
            high: this.getTasksByPriority('high').length,
            medium: this.getTasksByPriority('medium').length,
            low: this.getTasksByPriority('low').length
        };

        return {
            total,
            completed,
            pending,
            completionRate: total > 0 ? (completed / total * 100).toFixed(2) : 0,
            byPriority
        };
    }
}

// 使用範例
if (typeof module !== 'undefined' && module.exports) {
    module.exports = { Task, TaskManager };
}

// 範例使用
const manager = new TaskManager();

// 添加任務
manager.addTask('學習 GitHub Copilot', '完成基礎教程', 'high');
manager.addTask('撰寫專案文件', '更新 README', 'medium');
manager.addTask('程式碼重構', '優化現有程式碼', 'low');

// 完成一個任務
manager.completeTask(1);

// 顯示統計資訊
console.log('任務統計:', manager.getStatistics());
console.log('待處理任務:', manager.getPendingTasks().map(t => t.title));
